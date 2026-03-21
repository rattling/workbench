
# Stochastic Modelling Pattern Recognition Cheat Sheet

A quick reference for recognising common mathematical structures that appear in
random walks, Markov chains, diffusion models, and stochastic processes.

This sheet is meant to sit beside your main learning roadmap.

---

# Core Modelling Workflow

Almost every stochastic modelling problem follows this pipeline:

1. Define the quantity of interest (probability, expectation, etc)
2. Condition on the next step
3. Write a recurrence relation
4. Recognise the mathematical structure
5. Guess the function family
6. Apply boundary conditions

---

# Recurrence Pattern Recognition

## Pattern 1 — Constant First Difference

Equation form

f(i+1) − f(i) = constant

Interpretation

Slope is constant.

Solution shape

Linear

f(i) = ai + b

Appears in

- fair gambler’s ruin probability
- simple accumulation processes

---

## Pattern 2 — Constant Second Difference

Equation form

f(i+1) − 2f(i) + f(i−1) = constant

Interpretation

Curvature is constant.

Solution shape

Quadratic

f(i) = ai² + bi + c

Appears in

- expected hitting times
- diffusion approximations
- random walk stopping times

---

## Pattern 3 — Linear Recurrence

Equation form

a f(i+1) + b f(i) + c f(i−1) = 0

Interpretation

Neighbouring states determine value.

Typical guess

f(i) = r^i

Steps

1. Substitute r^i
2. Derive characteristic equation
3. Solve for r
4. Combine solutions

Solution shape

Exponential combinations

f(i) = A r₁^i + B r₂^i

Appears in

- biased gambler’s ruin
- birth–death processes
- population models

---

# Probability Modelling Patterns

## First-Step Analysis

General form

Quantity(state) =
Σ probability × quantity(next state)

Example

p_i = ½ p_{i+1} + ½ p_{i−1}

Interpretation

Future behaviour determines present value.

---

## Expected Value Recurrence

General pattern

E_i = immediate contribution + expected future value

Example

E_i = 1 + ½E_{i+1} + ½E_{i−1}

---

# Random Walk Intuition

Symmetric walk

No drift

Probability solution tends to be linear.

Biased walk

Drift present

Probability solution tends to be exponential.

---

# Boundary Conditions

Boundary conditions determine constants in solutions.

Example

f(0) = 0  
f(N) = 1

Use these to solve for unknown coefficients.

---

# Common Solution Shapes

| Structure | Typical solution |
|---|---|
| constant first difference | linear |
| constant second difference | quadratic |
| multiplicative recurrence | exponential |
| probability flow | recurrence relation |

---

# Where These Patterns Appear

Physics

- diffusion
- Brownian motion
- statistical mechanics

Finance

- barrier hitting probabilities
- option pricing approximations

AI / Reinforcement Learning

- Markov decision processes
- value functions

Operations Research

- queues
- birth–death systems

---

# Key Intuition

Instead of trying to manipulate equations blindly, ask:

What **shape of function** could satisfy this recurrence?

Once the shape is identified, the algebra becomes straightforward.
