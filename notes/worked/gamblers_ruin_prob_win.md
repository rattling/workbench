# Gambler's Ruin: Probability of Winning

Find the probability of reaching the target fortune $N$ before going broke, starting from fortune $i$.

## 1. Setup

### Problem definition

A gambler starts with fortune $i$ where $0 < i < N$.

At each step:
- With probability $\frac{1}{2}$, fortune increases by 1
- With probability $\frac{1}{2}$, fortune decreases by 1

The process stops when fortune reaches either:
- $0$ (ruin - lose)
- $N$ (target - win)

### Define the probability

Let $p_i$ = probability of reaching $N$ before $0$, starting from fortune $i$.

Boundary conditions:

$p_0 = 0$ (already ruined)

$p_N = 1$ (already won)

## 2. Set up equations using first-step analysis

### From fortune $i$

From state $i$, we must take one step to either $i+1$ or $i-1$.

> $i \xrightarrow{p=1/2} i+1$
>
> $i \xrightarrow{p=1/2} i-1$
>
> $p_i = \frac{1}{2}p_{i+1} + \frac{1}{2}p_{i-1}$

This is a recurrence relation for the probability.

## 3. Rearrange into a difference equation

Multiply both sides by 2:

$2p_i = p_{i+1} + p_{i-1}$

Rearrange:

$p_{i+1} - 2p_i + p_{i-1} = 0$

The second difference equals **zero**.

## 4. Recognize the structure

When the second difference equals zero, the solution must be **linear**.

This is simpler than the expected time problem, which had a constant second difference and quadratic solution.

Therefore, assume:

$p_i = ai + b$

## 5. Apply boundary conditions

From $p_0 = 0$:

$0 = a(0) + b$

$\implies b = 0$

From $p_N = 1$:

$1 = aN$

$\implies a = \frac{1}{N}$

## 6. Final solution

The probability of winning starting from fortune $i$ is:

$p_i = \frac{i}{N}$

## 7. Interpretation

This result has a beautiful simplicity:

- The probability of winning is **proportional to your current fortune**
- If you have half the target, you have a 50% chance
- If you have 10% of the target, you have a 10% chance

In a fair game, your probability of success is exactly your fraction of the total wealth.

## 8. Example

Let $N = 100$ (target fortune is 100).

Starting from $i = 25$:

$p_{25} = \frac{25}{100} = 0.25$

There is a **25% chance** of reaching 100 before going broke.

## 9. Contrast with expected time

Notice the difference in solution types:

| Problem | Second Difference | Solution Type | Formula |
|---------|-------------------|---------------|---------|
| Probability of winning | $= 0$ | Linear | $p_i = \frac{i}{N}$ |
| Expected time to absorption | $= -2$ | Quadratic | $e_i = i(N-i)$ |

Same setup, different questions, different mathematics.

This demonstrates why recognizing the second difference structure is so powerful.
