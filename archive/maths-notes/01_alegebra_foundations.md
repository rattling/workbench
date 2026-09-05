
# Algebra Backfill for Stochastic Modelling
*A compact toolkit for probability, random walks, and thermodynamic-style modelling*

---

## Purpose
This syllabus rebuilds the algebraic and structural tools needed to work comfortably with:

- Random walks
- Gambler’s ruin
- Stopping times
- Markov chains
- Simple thermodynamic models

The focus is **recognizing structure in equations and functions**, not just manipulating symbols.

Expected total time: **5–10 hours of focused backfill**.

---

# Pattern Cheat Sheet (Core Modelling Instincts)

These patterns appear constantly in probability, physics, and stochastic modelling.

## Function Shapes

| Function type | Form | Behaviour |
|---|---|---|
| Linear | f(i) = ai + b | constant slope |
| Quadratic | f(i) = ai² + bi + c | constant curvature |
| Exponential | f(i) = r^i | multiplicative growth/decay |

---

## Finite Difference Patterns

| Observation | Interpretation |
|---|---|
| first difference constant | linear function |
| second difference constant | quadratic function |
| third difference constant | cubic function |

Example:

Δf(i) = f(i+1) − f(i)

Δ²f(i) = f(i+1) − 2f(i) + f(i−1)

---

## Recurrence Recognition

| Recurrence pattern | Likely solution |
|---|---|
| f(i+1) − f(i) = constant | linear |
| f(i+1) − 2f(i) + f(i−1) = constant | quadratic |
| af(i+1) + bf(i) + cf(i−1) = 0 | exponential r^i |

---

## Modelling Workflow

Every stochastic modelling problem tends to follow this pipeline:

1. Define the quantity (probability, expectation, etc)
2. Write a first‑step equation
3. Rearrange into a recurrence
4. Recognize the function structure
5. Guess the function family
6. Use boundary conditions to determine constants

---

# Section 1 — Functions and Index Thinking

## Goal
Be comfortable treating formulas as **functions over an index variable**.

Example:

f(i) = 2i + 3

Then

f(i+1), f(i−1)

represent shifted inputs.

## Concepts

- Function notation
- Index variables
- Evaluating shifted functions
- Polynomial functions
- Exponential functions

Examples:

Linear

f(i) = ai + b

Quadratic

f(i) = ai² + bi + c

Exponential

f(i) = r^i

---

## Exercises

1. Compute f(i+1) and f(i−1) for:
   - f(i) = 2i + 5
   - f(i) = i²
   - f(i) = 3^i

2. Expand
   - (i+1)²
   - (i−1)²

3. For f(i)=2i²+3i compute
   - f(i+1)
   - f(i−1)

---

## Useful Search Terms

- “function notation algebra”
- “polynomial functions basics”
- “exponential functions algebra”

---

# Section 2 — Finite Differences (Discrete Calculus)

## Goal

Understand the discrete equivalent of derivatives.

---

## Concepts

First difference

Δf(i) = f(i+1) − f(i)

Second difference

Δ²f(i) = f(i+1) − 2f(i) + f(i−1)

---

## Exercises

1. Compute first differences for

- f(i)=3i+1
- f(i)=i²
- f(i)=2i²+3i

2. Compute second differences for

- f(i)=i²
- f(i)=3i²
- f(i)=i²+i

3. Show that the second difference of i² is constant.

---

## Useful Search Terms

- “finite differences mathematics”
- “discrete calculus”
- “difference tables”

---

# Section 3 — Quadratics and Roots

## Goal

Be fluent with quadratic equations and root structure.

---

## Concepts

Standard form

ax² + bx + c

Factored form

a(x−r₁)(x−r₂)

Product of roots

r₁ r₂ = c/a

---

## Exercises

1. Expand

- (x−3)(x+2)
- (x−4)²

2. Factor

- x² − 9
- x² − 5x + 6

3. If one root of 2x² − 5x + 3 = 0 is 1, find the other.

---

## Useful Search Terms

- “quadratic equations algebra”
- “factoring quadratics”
- “product of roots formula”

---

# Section 4 — Linear Recurrences

## Goal

Understand equations where values depend on neighbouring values.

These appear constantly in stochastic processes.

---

## Concepts

Example recurrence

f(n+1) = 2f(n)

Second order recurrence

f(n+1) = 3f(n) − 2f(n−1)

Characteristic equation method.

---

## Exercises

1. Solve

f(n+1) = 2f(n)

2. Solve

f(n+1) = f(n) + 3

3. For

f(n+1) = 3f(n) − 2f(n−1)

derive the characteristic equation.

---

## Useful Search Terms

- “linear recurrence relations”
- “characteristic equation recurrence”
- “difference equations”

---

# Section 5 — Boundary Conditions

## Goal

Understand how constraints determine constants.

---

## Concepts

Example

f(i) = Ai + B

If

f(0)=0 and f(N)=1

then solve for A and B.

---

## Exercises

1. If f(i)=Ai+B and

f(0)=2  
f(5)=12

find A and B.

2. If f(i)=Ai²+Bi+C and

f(0)=0  
f(10)=0

express f(i) in simplified form.

---

# Section 6 — Stochastic Modelling Applications

## Example Problems

- Gambler’s ruin probability (fair coin)
- Gambler’s ruin probability (biased coin)
- Expected time to absorption
- Simple random walk behaviour

---

## Exercises

1. Derive the recurrence for gambler’s ruin probability.

2. Show the fair case leads to a linear solution.

3. Show expected time satisfies a second‑difference equation.

---

# Section 7 — Connection to Physics / Thermodynamics

Random walks appear in many physical systems.

Examples:

- diffusion
- heat flow
- particle motion
- entropy processes

---

## Useful Search Terms

- “random walk diffusion equation”
- “statistical mechanics random walk”
- “random walk physics explanation”

---

# Common Course Names (Helpful Resource Handles)

When searching learning materials, these topics are usually under:

### Algebra Foundations

- Algebra I
- Algebra II
- Pre‑Calculus

### Discrete Mathematics

- Discrete Mathematics
- Discrete Structures
- Difference Equations

### Probability / Stochastic Processes

- Intro to Probability
- Stochastic Processes
- Markov Chains

### Physics / Applied Math

- Mathematical Methods for Physics
- Statistical Mechanics
- Random Walk Theory

---

# Good Free Resources

Search for:

- “Paul's Online Math Notes algebra”
- “MIT OpenCourseWare discrete mathematics”
- “MIT probability course random walk”
- “Khan Academy Algebra II”

---

# Expected Outcome

After completing this backfill you should be comfortable:

- manipulating indexed functions
- recognizing linear / quadratic / exponential structures
- computing finite differences
- solving simple recurrence relations
- applying boundary conditions
- deriving simple stochastic models

