"""
Demand process generator

Produces deterministic demand sequence with sinusoidal pattern + noise.
Ensures both policies see the same realized demand for fair comparison.
"""

import math
import random


def generate_demands(T: int, seed: int) -> list[float]:
    """
    Generate demand sequence with weekly seasonality.

    Model: D_t = 80 + 20*sin(2πt/7) + ε_t
    where ε_t ~ Normal(0, 10)

    Args:
        T: Number of time periods
        seed: Random seed for reproducibility

    Returns:
        List of demand values (length T)
    """
    random.seed(seed)
    demands = []

    for t in range(T):
        # Base demand with weekly cycle
        base = 80.0
        seasonal = 20.0 * math.sin(2 * math.pi * t / 7)
        noise = random.gauss(0, 10)

        demand = base + seasonal + noise
        demands.append(max(0, demand))  # Demand cannot be negative

    return demands
