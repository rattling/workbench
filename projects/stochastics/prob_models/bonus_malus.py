"""Bonus-Malus insurance ladder (Ross Example 4.4-ish, the one that fought back).

Two primitives with different citizenship:
  - NATURE:  claims per year ~ Poisson(lam). Estimated, falsifiable.
  - POSITED: the transition rule s(i, k) - the company's designed table.
The transition matrix P is MANUFACTURED from them:
  P[i][j] = sum of Poisson masses over every k that the rule routes i -> j.
("Sum the likelihoods of all the k's that bring you from i to j.")
"""

from math import exp, factorial

import numpy as np

PREMIUMS = np.array([200.0, 250.0, 400.0, 600.0])
N_STATES = 4  # states 1..4 internally indexed 0..3


def rule(i: int, k: int) -> int:
    """The posited table: next state from state i (0-indexed) with k claims.
    Zero claims: down one rung, floor at 0. k claims: up k rungs, cap at 3."""
    if k == 0:
        return max(i - 1, 0)
    return min(i + k, N_STATES - 1)


def poisson_pmf(k: int, lam: float) -> float:
    return exp(-lam) * lam**k / factorial(k)


def build_matrix(lam: float = 1.0, k_max: int = 60) -> np.ndarray:
    """Push the Poisson through the rule. k_max truncates the dummy-variable
    loop; the tail beyond 60 is astronomically small for sane lam."""
    P = np.zeros((N_STATES, N_STATES))
    for i in range(N_STATES):
        for k in range(k_max):
            P[i, rule(i, k)] += poisson_pmf(k, lam)
    # checksum: every row must be a probability distribution
    assert np.allclose(P.sum(axis=1), 1.0), "a k was mislaid - rows must sum to 1"
    return P


def stationary(P: np.ndarray) -> np.ndarray:
    n = P.shape[0]
    A = np.eye(n) - P.T + np.ones((n, n))
    return np.linalg.solve(A, np.ones(n))


def average_premium(lam: float = 1.0) -> float:
    """The business number the whole apparatus exists to compute."""
    return float(stationary(build_matrix(lam)) @ PREMIUMS)


def simulate(lam: float, n_years: int, rng=None) -> np.ndarray:
    """Third road: simulate a policyholder's lifetime, count time-shares."""
    rng = rng or np.random.default_rng()
    s, hist = 0, np.empty(n_years, dtype=int)
    for t in range(n_years):
        s = rule(s, rng.poisson(lam))
        hist[t] = s
    return hist


if __name__ == "__main__":
    lam = 1.0
    P = build_matrix(lam)
    print("P (lam=1):")
    print(P.round(4))

    pi = stationary(P)
    print("pi by solve:   ", pi.round(4))

    pi_pow = np.linalg.matrix_power(P, 100)[0]
    print("pi by powers:  ", pi_pow.round(4))

    hist = simulate(lam, 200_000, rng=np.random.default_rng(1))
    pi_sim = np.bincount(hist, minlength=4) / len(hist)
    print("pi by simulate:", pi_sim.round(4))

    print(f"average premium per policyholder: {pi @ PREMIUMS:.2f}")
