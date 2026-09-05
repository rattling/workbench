# Canonical Problems and Pattern Recognition in Stochastic Modelling

This note is a compact touchstone for the core problems and modelling moves that recur across stochastic processes.

## Why this matters

Most applied stochastic models reduce to a small set of reusable ideas:

- first-step conditioning
- recurrence setup
- recognising solution shape
- boundary/normalization constraints

If these feel natural, advanced topics become much easier.

## The core modelling move

When you derive a recurrence, the key question is:

**What type of function is the solution likely to be?**

For 1D discrete-state problems, this often comes down to pattern recognition in finite differences.

### Shape-recognition cheat sheet

| Recurrence pattern | Typical solution shape | Where it appears |
|---|---|---|
| $f_{i+1} - f_i = c$ | linear | hitting probabilities, drift balances |
| $f_{i+1} - 2f_i + f_{i-1} = c$ | quadratic | expected absorption times |
| $f_{i+1} = k f_i$ or homogeneous 2nd-order with non-symmetric coefficients | exponential / geometric mix | biased walks, ruin with $p \neq q$ |

This is the discrete analogue of:

- $f''(x)=0 \Rightarrow$ linear
- $f''(x)=\text{const} \Rightarrow$ quadratic

## Canonical problem set

## 1) Waiting time to first success

**Prototype question**

- Repeated coin flips: expected flips until first head.

**Main tool**

- geometric distribution and memorylessness.

**Why it matters**

- establishes stopping-time expectations with minimal state.

---

## 2) Waiting time for a pattern

**Prototype question**

- Expected time to see HTH (or HHH, HTT, etc.).

**Main tool**

- finite-state Markov representation of partial matches.

**Why it matters**

- teaches state design and first-step equations for pattern processes.

---

## 3) Pattern race (competing motifs)

**Prototype question**

- Probability HTH appears before HHH.

**Main tool**

- absorbing Markov chain over overlap states.

**Why it matters**

- introduces competing absorbing events and race probabilities.

---

## 4) Random walk on integers

**Prototype question**

- Position after $t$ steps, drift, and spread under $+1/-1$ moves.

**Main tool**

- increments, expectation/variance evolution.

**Why it matters**

- baseline for diffusion intuition and scaling.

---

## 5) Gambler's ruin (fair walk)

**Prototype questions**

- Win probability before ruin.
- Expected time to absorption.

**Main tools**

- boundary value recurrences on $\{0,1,\dots,N\}$.

**Key forms (fair case $p=q=1/2$)**

- Win probability: $\pi_i = i/N$ (linear).
- Expected absorption time: $e_i = i(N-i)$ (quadratic).

**Why it matters**

- cleanest setting for recurrence + boundary-condition solving.

---

## 6) Gambler's ruin (biased walk)

**Prototype question**

- Same as above but $p \neq q$.

**Main tool**

- characteristic equation / geometric terms.

**Key insight**

- fairness gives polynomial structure; bias introduces exponential structure.

---

## 7) Stationary distribution for finite Markov chains

**Prototype question**

- Long-run state proportions from transition matrix $P$.

**Main tool**

- solve $\pi = \pi P$ with normalization $\sum_i \pi_i = 1$.

**Why it matters**

- separates transient behavior from long-run equilibrium behavior.

---

## 8) Birth-death processes

**Prototype question**

- Population/queue level with nearest-neighbor up/down transitions.

**Main tool**

- local balance, detailed balance (when available), hitting/extinction analysis.

**Why it matters**

- direct bridge to queues and continuous-time Markov chains.

---

## 9) Diffusion limit and Brownian scaling

**Prototype question**

- How random walks converge under rescaling.

**Main tool**

- CLT-level scaling intuition and weak convergence ideas.

**Why it matters**

- connects microscopic random steps to macroscopic PDE/physics behavior.

---

## 10) Monte Carlo estimation

**Prototype question**

- Estimate hitting probabilities or expected times by simulation.

**Main tool**

- sampling, confidence/error scaling, variance reduction awareness.

**Why it matters**

- practical validation for models and formulas.

## Reusable workflow (for most exercises)

1. Define the quantity of interest ($\pi_i$, $e_i$, etc.).
2. Write first-step equation from one-step transitions.
3. Rearrange recurrence to expose structure (difference form).
4. Guess solution family (linear/quadratic/exponential).
5. Apply boundary and normalization constraints.
6. Sanity-check shape and edge cases.

## Fast sanity checks

- Boundary values are exact and match the process definition.
- Probabilities stay in $[0,1]$.
- Expected times are nonnegative.
- Symmetry/fairness cases reduce to simple forms.
- Middle states often maximize absorption time in fair bounded walks.

## Field-level takeaway

A large fraction of early stochastic modelling is pattern recognition on recurrences:

- identify the operator,
- infer the solution family,
- pin constants with constraints.

That shift—from algebra-first to structure-first—is the core modelling skill.
