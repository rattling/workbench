# Gambler's Ruin: Expected Time to Absorption

Find the expected number of steps until a gambler's fortune reaches either ruin (0) or a target fortune (N) in a fair random walk.

## 1. Setup

### Problem definition

A gambler starts with fortune $i$ where $0 < i < N$.

At each step:
- With probability $\frac{1}{2}$, fortune increases by 1
- With probability $\frac{1}{2}$, fortune decreases by 1

The process stops when fortune reaches either:
- $0$ (ruin)
- $N$ (target)

### Define the expected value

Let $e_i$ = expected number of steps to absorption starting from fortune $i$.

Boundary conditions:

$e_0 = 0$

$e_N = 0$

## 2. Set up equations using first-step analysis

### From fortune $i$

From state $i$, we must take one step to either $i+1$ or $i-1$.

> $i \xrightarrow{p=1/2} i+1$
>
> $i \xrightarrow{p=1/2} i-1$
>
> $e_i = 1 + \frac{1}{2}e_{i+1} + \frac{1}{2}e_{i-1}$

This is a **recurrence relation** for the expected time.

## 3. Rearrange into a difference equation

Multiply both sides by 2:

$2e_i = 2 + e_{i+1} + e_{i-1}$

Rearrange:

$e_{i+1} - 2e_i + e_{i-1} = -2$

The left side is the **second discrete difference** of $e_i$.

## 4. Recognize the structure

The key insight: if the second difference is **constant**, the function must be **quadratic**.

This mirrors calculus: constant second derivative → quadratic function.

Therefore, assume:

$e_i = ai^2 + bi + c$

For a quadratic $ai^2 + bi + c$, the second difference is:

$\text{second difference} = 2a$

From our equation:

$2a = -2 \implies a = -1$

So the function has the form:

$e_i = -i^2 + Bi + C$

## 5. Apply boundary conditions

From $e_0 = 0$:

$0 = -0^2 + B(0) + C$

$\implies C = 0$

From $e_N = 0$:

$0 = -N^2 + BN$

$\implies B = N$

## 6. Final solution

The expected time to absorption starting from fortune $i$ is:

$e_i = -i^2 + Ni = i(N - i)$

## 7. Interpretation

Properties of the solution:

- Expected time is $0$ at the boundaries
- Maximized at the middle: $e_{N/2} = \frac{N^2}{4}$
- The curve is quadratic and concave downward

Intuition: starting near the middle takes longest on average to hit either boundary.

## 8. Example

Let $N = 10$ (target fortune is 10).

Starting from $i = 5$:

$e_5 = 5(10 - 5) = 5 \times 5 = 25$

On average, it takes **25 steps** to reach either ruin or a fortune of 10.

## 9. General technique learned

This problem demonstrates a reusable approach:

1. **Define the quantity** of interest (here: expected time $e_i$)
2. **Write a first-step equation** using the Markov property
3. **Rearrange into a difference equation**
4. **Recognize the structure** (constant second difference → quadratic)
5. **Solve using boundary conditions**

This same technique applies to many stochastic processes.
