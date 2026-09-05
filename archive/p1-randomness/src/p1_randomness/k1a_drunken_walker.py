"""
Drunken Walker Part A — first contact.

A walker starts at 0. Each step: flip a fair coin, move +1 or -1.

A1. One walker, 100 steps — watch the path unfold every 10 steps.
A2. One walker, 1000 steps — where do they end up? Run a few times.
A3. Ten walkers, 1000 steps — all final positions on one line.
     Prediction before running: where do you expect most to end up?
A4. 1000 walkers, 1000 steps — histogram of final positions.
     What shape is it? Range? Anyone near ±100? ±500?

Before moving to Part B, write down:
  1. The average final position across 1000 walkers is close to ___ because ___
  2. The spread covers roughly ±___ (is it ±10, ±30, or ±100?)
"""

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


# --- A1: one walker, 100 steps, print every 10 ---
print("=== A1: one walker, 100 steps ===")
pos = 0
for step in range(1, 101):
    pos += random.choice([-1, 1])
    if step % 10 == 0:
        print(f"  step {step:>3}: pos = {pos:+}")

# --- A2: one walker, 1000 steps ---
print("\n=== A2: one walker, 1000 steps ===")
pos = sum(random.choices([-1, 1], k=1000))
print(f"  final position: {pos:+}")

# --- A3: ten walkers, 1000 steps ---
print("\n=== A3: ten walkers, 1000 steps ===")
final_positions = [sum(random.choices([-1, 1], k=1000)) for _ in range(10)]
print("  " + "  ".join(f"{p:+}" for p in final_positions))

# --- A4: 1000 walkers, 1000 steps — histogram ---
print("\n=== A4: 1000 walkers, 1000 steps ===")
final_positions = [sum(random.choices([-1, 1], k=1000)) for _ in range(1000)]
ascii_hist(final_positions)
