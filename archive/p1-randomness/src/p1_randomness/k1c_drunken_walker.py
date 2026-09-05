"""
Drunken Walker Part C — first passage times.

How long does a walker take to reach a target distance d for the first time?

--- What we found ---

The distribution is sharply right-skewed — median << mean — for every target:

  Target | Median | Mean
  -------|--------|------
       5 |     ~25|  ~100+
      10 |    ~100|  ~500+
      20 |    ~400| ~2000+
      40 |   ~1600| ~8000+

Median scales as d², mean is much larger (theoretically infinite for an
uncapped walk). The histogram has a hard left edge at d (the minimum possible
steps) and a very long right tail.

--- Why the skew ---

To arrive in exactly d steps you need every step to go the right way — one
path out of 2^d possibilities. Every detour requires extra steps to recover,
and recovery can itself go wrong. The number of ways to take a long winding
path vastly outnumbers the short direct ones, creating the heavy right tail.

--- Why median ~ d² ---

From Part B: after n steps, std dev of position ≈ √n. Inverting — to reach
position d, expect to need n ≈ d² steps. Doubling the target quadruples the
typical passage time.

--- The distribution ---

This is the inverse Gaussian / Lévy distribution. It is a stable distribution
with infinite mean — the few walkers that wander for a very long time dominate
the average even as the sample size grows.

References:
  - Variance of a sum: Var(X₁+…+Xₙ) = n·Var(X₁) for independent steps
    → std dev ∝ √n  (Blitzstein Ch. 7)
  - Why positions approach Gaussian: Central Limit Theorem (Blitzstein Ch. 10.3)
  - First passage times: Grinstead & Snell Ch. 12
"""

import random
import statistics


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


targets = [5, 10, 20, 40]
walkers = 1000


# --- A1: one walker, 100 steps, print every 10 ---
print("=== Passage Times ===")
pos = 0

for target in targets:
    passage_times = []
    for _ in range(walkers):
        step_count = 0
        pos = 0
        while step_count <= 100000:
            step_count += 1
            pos += 1 if random.random() > 0.5 else -1
            if pos == target:
                passage_times.append(step_count)
                break
    print(f"Passage Times for Target: {target}")
    print(
        f"Mean:{sum(passage_times) / len(passage_times)}\nMedian:{statistics.median(passage_times)}\nMax:{max(passage_times)}\n"
    )
    print(f"Fails: {walkers - len(passage_times)}\n")
    ascii_hist(passage_times)
