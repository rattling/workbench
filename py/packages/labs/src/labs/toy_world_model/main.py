 # %%


"""toy-world-model"""

import numpy as np
import plotly.graph_objects as go
import torch
import torch.nn as nn
from pysr import PySRRegressor


TOTAL_TIME = 6.0
DT = .1
N_STEPS = int(TOTAL_TIME / DT)


def step(state, action):
    """
    True world dynamics.
    state = [x, v]
    action = force/acceleration
    """
    x, v = state

    v_next = v + action * DT
    x_next = x + v_next * DT

    return np.array([x_next, v_next], dtype=np.float32)


def rollout_true(initial_state, actions):
    states = [initial_state]

    state = initial_state
    for action in actions:
        state = step(state, action)
        states.append(state)

    return np.array(states)


def make_training_data(n_samples=10_000):
    """
    Generate random one-step transitions:
    [x_t, v_t, a_t] -> [x_{t+1}, v_{t+1}]

    We sample states randomly across a wide range rather than following a
    single trajectory. This gives the model diverse coverage of the state
    space so it generalises, rather than only knowing one narrow path.
    """
    X = []
    y = []

    for _ in range(n_samples):
        state = np.array([
            np.random.uniform(-10, 10),
            np.random.uniform(-5, 5),
        ], dtype=np.float32)

        action = np.random.uniform(-2, 2)
        next_state = step(state, action)

        # Input:  [x, v, action]  — everything the model needs to predict one step
        # Output: [dx, dv]  — the *change* in state, not the absolute next state.
        # Predicting deltas is better because:
        #   - the target values are small (close to zero), which is easier to learn
        #   - the network only needs to learn "what changes", not "where you end up"
        #   - it biases the model toward continuity: if it predicts ~0 change it
        #     at least won't teleport the state somewhere random
        delta = next_state - state
        X.append([state[0], state[1], action])
        y.append(delta)

    return (
        torch.tensor(np.array(X), dtype=torch.float32),
        torch.tensor(np.array(y), dtype=torch.float32),
    )


class WorldModel(nn.Module):
    """
    A small feedforward neural network that learns to predict the *delta* —
    the change in state — given the current state and action: f(x, v, a) -> (dx, dv).
    The next state is then computed as: next_state = state + predicted_delta.

    Architecture:
        input (3)  ->  hidden (32)  ->  hidden (32)  ->  output (2)

    - Linear layers learn a weighted sum of their inputs + a bias.
    - Tanh activations introduce non-linearity between layers. Without them
      the whole network would collapse to a single linear transformation,
      which is already the true dynamics — but in general we want the network
      to be able to approximate arbitrary functions.
    - No activation on the final layer: the output is a raw real-valued
      prediction, not a probability, so we don't want to squash it.
    """
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            # Layer 1: 3 inputs -> 32 hidden units
            # Learns combinations of (x, v, action) that are useful features
            nn.Linear(3, 32),
            nn.Tanh(),
            # Layer 2: 32 -> 32, deepens the representation
            nn.Linear(32, 32),
            nn.Tanh(),
            # Output layer: 32 -> 2 (predicts x_next, v_next)
            nn.Linear(32, 2),
        )

    def forward(self, x):
        # x shape: (batch_size, 3)  ->  output shape: (batch_size, 2)
        return self.net(x)


def train_model():
    X, y = make_training_data()

    model = WorldModel()

    # Adam: an adaptive gradient descent optimiser. It tracks a running average
    # of past gradients and their squares, so it effectively sets a per-parameter
    # learning rate. Much more robust than plain SGD for this kind of problem.
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # MSE loss: mean squared error between predicted and true next state.
    # Penalises large errors more than small ones (squared), which is natural
    # for a regression problem like this.
    loss_fn = nn.MSELoss()

    for epoch in range(5000):
        # Forward pass: run the whole dataset through the network
        pred = model(X)

        # Compare predictions to true next states
        loss = loss_fn(pred, y)

        # Backward pass:
        # 1. zero_grad() clears gradients from the previous step (they accumulate
        #    by default in PyTorch, so we must reset each iteration)
        # 2. loss.backward() computes d(loss)/d(every parameter) via backprop
        # 3. optimizer.step() nudges each parameter in the direction that reduces loss
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 100 == 0:
            print(f"epoch {epoch}, loss = {loss.item():.6f}")

    return model


def rollout_learned(model, initial_state, actions):
    """
    Roll out a trajectory using the learned world model instead of true dynamics.
    Each step feeds the model's own prediction back in as the next state —
    so errors compound over time. This is called "closed-loop" or "autoregressive"
    rollout and is the real test of whether the model has learned the dynamics.
    """
    states = [initial_state]

    state = initial_state.astype(np.float32)

    for action in actions:
        # Pack current state + action into a (1, 3) tensor — the "1" is a batch
        # dimension that PyTorch expects even when we're only doing one sample
        model_input = torch.tensor(
            [[state[0], state[1], action]],
            dtype=torch.float32,
        )

        # torch.no_grad() tells PyTorch not to build a computation graph here.
        # We're just doing inference (not training), so we don't need gradients.
        # This saves memory and is faster.
        with torch.no_grad():
            # Model predicts the delta; add it to current state to get next state
            delta = model(model_input).numpy()[0]
            next_state = state + delta

        states.append(next_state)
        state = next_state  # feed the prediction back in for the next step

    return np.array(states)


def probe_learned_transitions(model):
    """
    Use the Jacobian of the network to recover the transition coefficients it learned.

    The model now predicts deltas, so the true Jacobian (d delta / d input) is:
        d(dx)/d(x) = 0          d(dx)/d(v) = DT       d(dx)/d(a) = DT^2
        d(dv)/d(x) = 0          d(dv)/d(v) = 0        d(dv)/d(a) = DT

    (The state terms drop out because dx = x_next - x, so the x dependence cancels.)

    We evaluate the Jacobian at the origin — for a linear system the Jacobian
    is the same everywhere, so the point doesn't matter.
    """
    # Evaluate at origin — shape (1, 3)
    inp = torch.zeros(1, 3, requires_grad=True)

    # jacobian() returns a tensor of shape (1, 2, 1, 3):
    #   [batch_out, output_dim, batch_in, input_dim]
    # We squeeze out the batch dims to get a clean (2, 3) matrix.
    jac = torch.autograd.functional.jacobian(model, inp)
    jac = jac.squeeze()  # shape: (2, 3)

    learned = jac.numpy()

    # The true coefficient matrix for the *delta* targets
    true = np.array([
        [0.0,  DT,   DT**2],   # dx = 0*x + DT*v + DT^2*a
        [0.0,  0.0,  DT   ],   # dv = 0*x + 0*v  + DT*a
    ])

    print("\n--- Learned transition coefficients (Jacobian at origin) ---")
    print(f"{'':12s}  {'x':>10s}  {'v':>10s}  {'a':>10s}")
    for row_name, learned_row, true_row in zip(["dx", "dv"], learned, true):
        learned_str = "  ".join(f"{v:+.4f}" for v in learned_row)
        true_str    = "  ".join(f"{v:+.4f}" for v in true_row)
        print(f"  {row_name}:  learned [{learned_str}]  true [{true_str}]")

    print(f"\n  Max coefficient error: {np.abs(learned - true).max():.6f}")


def symbolic_regression(n_samples=2000):
    """
    Use PySR to search for symbolic expressions that describe the transitions.

    Rather than probing the neural network, we go straight to the raw data —
    sample random (x, v, action) inputs, compute the true deltas, and ask PySR
    to find simple equations that fit them.

    PySR runs an evolutionary algorithm (it actually calls Julia under the hood)
    that builds expression trees from basic operations (+, *, constants...) and
    evolves them to minimise prediction error while keeping expressions short.
    The result is a Pareto front: simple-but-less-accurate vs complex-but-accurate.
    Ideally the true equations sit right on that front.
    """
    # Generate input data: random (x, v, action) triples
    rng = np.random.default_rng(0)
    x       = rng.uniform(-10, 10, n_samples).astype(np.float32)
    v       = rng.uniform(-5,   5, n_samples).astype(np.float32)
    action  = rng.uniform(-2,   2, n_samples).astype(np.float32)

    # Compute true deltas for each sample
    states  = np.stack([x, v], axis=1)
    deltas  = np.array([
        step(states[i], action[i]) - states[i]
        for i in range(n_samples)
    ], dtype=np.float32)

    # X matrix: each row is [x, v, action]
    X = np.stack([x, v, action], axis=1)

    print("\n--- Symbolic regression for dx ---")
    # niterations: how long to search — more = better equations, slower
    # binary_operators/unary_operators: the building blocks PySR can use
    sr_dx = PySRRegressor(
        niterations=40,
        binary_operators=["+", "*"],
        unary_operators=[],
        verbosity=0,
    )
    sr_dx.fit(X, deltas[:, 0], variable_names=["x", "v", "a"])
    print(sr_dx)

    print("\n--- Symbolic regression for dv ---")
    sr_dv = PySRRegressor(
        niterations=40,
        binary_operators=["+", "*"],
        unary_operators=[],
        verbosity=0,
    )
    sr_dv.fit(X, deltas[:, 1], variable_names=["x", "v", "a"])
    print(sr_dv)

    return sr_dx, sr_dv


if __name__ == "__main__":
    model = train_model()

    probe_learned_transitions(model)

    symbolic_regression()

    initial_state = np.array([0.0, 0.0], dtype=np.float32)

    half = N_STEPS // 2
    actions = np.array([1.0] * half + [-1.0] * (N_STEPS - half), dtype=np.float32)

    true_states = rollout_true(initial_state, actions)
    learned_states = rollout_learned(model, initial_state, actions)

    time = np.arange(len(true_states)) * DT

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=true_states[:, 0], mode="lines", name="true position"))
    fig.add_trace(go.Scatter(x=time, y=learned_states[:, 0], mode="lines", name="learned position", line=dict(dash="dash")))
    fig.add_trace(go.Scatter(x=time, y=true_states[:, 1], mode="lines", name="true velocity"))
    fig.add_trace(go.Scatter(x=time, y=learned_states[:, 1], mode="lines", name="learned velocity", line=dict(dash="dash")))
    fig.update_layout(title="True World vs Learned World Model", xaxis_title="time", hovermode="x unified")
    fig.show()


