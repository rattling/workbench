"""
Drunken Walker — building intuition for the sqrt(n) diffusion law.

A walker takes n steps, each ±1 with equal probability. The question is:
how far from the start do we expect to end up after n steps?

Naive intuition says steps cancel out so displacement ~ 0. That's true for
the *mean* — positive and negative steps balance on average. But the *spread*
(std dev) of final positions across many walks grows as sqrt(n), not n.

This is because individual steps don't cancel perfectly — there's leftover
random imbalance, and that imbalance scales with sqrt(n). Doubling the number
of steps doubles the time but only increases spread by ~1.4x (sqrt(2)).

Key result:  std_dev(final position) ≈ sqrt(n)

This shows up everywhere: Brownian motion, diffusion in physics, the standard
error of a sample mean, volatility scaling in finance (sigma * sqrt(T)).

Sample output (1000 walks per step count):

   Steps |     Mean |  Std Dev | sqrt(n)
---------+----------+----------+--------
     100 |    -0.40 |     9.78 |   10.00
     400 |     0.37 |    19.73 |   20.00
     900 |    -0.43 |    29.33 |   30.00
    1600 |    -0.79 |    41.36 |   40.00
"""

import math
import random


def ascii_hist(values, bins=20, width=40):
    lo, hi = min(values), max(values)
    if lo == hi:
        print(f"All values: {lo}")
        return
    bin_size = (hi - lo) / bins
    counts = [0] * bins
    for v in values:
        idx = min(int((v - lo) / bin_size), bins - 1)
        counts[idx] += 1
    max_count = max(counts)
    for i, c in enumerate(counts):
        label = f"{lo + i * bin_size:+7.1f}"
        bar = "#" * int(c / max_count * width)
        print(f"{label} | {bar} ({c})")


num_walks = 1000
step_counts = [100, 400, 900, 1600]

means = []
stds = []

for n_steps in step_counts:
    final_positions = []
    for _ in range(num_walks):
        pos = sum(random.choices([-1, 1], k=n_steps))
        final_positions.append(pos)

    ascii_hist(final_positions)
    mean = sum(final_positions) / len(final_positions)
    std = math.sqrt(sum((x - mean) ** 2 for x in final_positions) / (len(final_positions) - 1))
    means.append(mean)
    stds.append(std)


print(f"{'Steps':>8} | {'Mean':>8} | {'Std Dev':>8}")
print(f"{'-' * 8}-+-{'-' * 8}-+-{'-' * 8}")
for n_steps, mean, std in zip(step_counts, means, stds):
    print(f"{n_steps:>8} | {mean:>8.2f} | {std:>8.2f}")
