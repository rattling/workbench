# Toy World Model — Findings

A minimal experiment in learning physics from data, then recovering
the underlying equations symbolically.

## Setup

A 1D point-mass system with state $[x, v]$ and scalar action $a$ (acceleration):

$$x_{t+1} = x_t + (v_t + a \cdot \Delta t) \cdot \Delta t$$
$$v_{t+1} = v_t + a \cdot \Delta t$$

Parameters: $\Delta t = 0.1$, $T = 6.0\,\text{s}$, $N = 60$ steps.

---

## Step 1 — Neural World Model

A feedforward network $f(x, v, a) \to (\Delta x, \Delta v)$ trained on 10,000
random one-step transitions sampled uniformly across the state space.

**Architecture:** input(3) → Linear(32) → Tanh → Linear(32) → Tanh → Linear(2)

**Key design choice — predict deltas, not absolute next state.**  
The targets $(\Delta x, \Delta v)$ are small and centred near zero, which is easier
to learn. It also biases the model toward continuity: a network that predicts zero
change is wrong but at least doesn't teleport the state.

At inference time: $s_{t+1} = s_t + f(s_t, a_t)$

**Result:** after 5000 epochs (Adam, lr=0.001, MSE loss), the learned rollout
tracks the true trajectory almost exactly over the full 6-second horizon.

---

## Step 2 — Recovering Equations via Jacobian

Because the true dynamics are linear, the Jacobian of the network
$\partial(\Delta x, \Delta v) / \partial(x, v, a)$ evaluated at any point
recovers the transition coefficients directly.

**True coefficients:**

|        |  $x$  |  $v$      | $a$        |
|--------|-------|-----------|------------|
| $dx$   | 0     | $\Delta t$  | $\Delta t^2$ |
| $dv$   | 0     | 0         | $\Delta t$   |

With $\Delta t = 0.1$: $dx$ coefficients are `[0, 0.1, 0.01]`, $dv$ is `[0, 0, 0.1]`.

**Learned coefficients matched the true values to ~4 decimal places** (max error < 0.001).

The network has no concept of physics — gradient descent simply converged onto
the only function that consistently explains all 10,000 transitions. The result
happens to be Newton's equations.

---

## Step 3 — Symbolic Regression via PySR

Rather than probing the neural network, PySR was applied directly to the raw
transition data. PySR runs an evolutionary search over expression trees using
$\{+, \times\}$ as operators, producing a Pareto front of equations
ranked by simplicity vs accuracy.

**Result for $dx$:** the selected equation was

$$dx = (a \cdot 0.1 + v) \cdot 0.1 = 0.1v + 0.01a$$

which is exactly $\Delta t \cdot v + \Delta t^2 \cdot a$.

**Result for $dv$:** converged to $dv = 0.1 \cdot a = \Delta t \cdot a$.

The score column in the Pareto table shows the log-improvement per unit of added
complexity. Both equations appear as a sharp spike (score ~11 for $dx$, large for $dv$)
with all subsequent more-complex rows scoring near zero — meaning extra terms are
fitting noise, not signal. The true physics sits cleanly at the elbow.

---

## Summary

| Method | What it finds | How |
|--------|--------------|-----|
| Neural net rollout | Accurate trajectory prediction | Minimises MSE over transitions |
| Jacobian probe | Numerical transition coefficients | Automatic differentiation through trained weights |
| PySR | Human-readable symbolic equations | Evolutionary search over expression trees |

All three approaches independently recover the same underlying physics from data alone,
each giving a different level of interpretability vs complexity.
