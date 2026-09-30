"""Bunker-price regime model — a 3-state Markov chain. The founding example.

Bunker fuel prices don't move the same way all the time; they drift between
qualitatively different *regimes*:

    0  Quiet     — prices barely move
    1  Trending  — a sustained directional drift
    2  Volatile  — large, erratic swings

Each step the market jumps according to the row of ``T`` for the current state:

                 -> Quiet  Trending  Volatile
    from Quiet    [  0.90     0.08      0.02  ]
    from Trending [  0.20     0.70      0.10  ]
    from Volatile [  0.10     0.30      0.60  ]

The chain is "sticky": every regime most likely stays put (heavy diagonal), so
the market lingers before switching — the clustering you see in real price
series (quiet stretches, trending runs, bursts of volatility).

Questions this module answers, each by simulation AND by theory:

    1. Long-run mix — what fraction of time in each regime? (stationary π,
       reachable three ways: simulate / matrix powers / linear solve)
    2. Mean first passage — from Volatile, how long until the market calms?
    3. How long do turbulent spells last, under three different definitions:
       a. ``storm_lengths``            — Volatile onset until Quiet, tolerating
                                         Trending dips in between
       b. ``spell_lengths``            — an unbroken run of Volatile days
       c. ``volatile_days_per_excursion`` — within each departure from Quiet and
                                         back, how many days were Volatile

Every function here was originally written (and debugged) by hand; see
``notes/LORE.md`` for the bugs, which were half the curriculum. The three spell
definitions are not redundant — (c) is the one that forced the flag/counter
separation, and it is where both first-passage bugs lived.
"""

import numpy as np

LABELS = ["Quiet", "Trending", "Volatile"]

T = np.array(
    [
        [0.90, 0.08, 0.02],  # from Quiet
        [0.20, 0.70, 0.10],  # from Trending
        [0.10, 0.30, 0.60],  # from Volatile
    ]
)


def simulate(
    P: np.ndarray,
    n_steps: int,
    start: int | None = None,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """One long path of the chain. Returns array of state indices."""
    rng = rng or np.random.default_rng()
    n = P.shape[0]
    s = start if start is not None else rng.integers(n)
    hist = np.empty(n_steps, dtype=int)
    for t in range(n_steps):
        s = rng.choice(n, p=P[s])
        hist[t] = s
    return hist


def empirical_distribution(hist: np.ndarray, n_states: int) -> np.ndarray:
    """Fraction of time spent in each state (road 1 to π)."""
    counts = np.bincount(hist, minlength=n_states)
    return counts / len(hist)


def stationary_by_power(P: np.ndarray, n: int = 100) -> np.ndarray:
    """Row of Pⁿ for large n (road 2 to π: Chapman-Kolmogorov + convergence)."""
    return np.linalg.matrix_power(P, n)[0]


def stationary_by_solve(P: np.ndarray) -> np.ndarray:
    """Exact fixed point πP = π with sum(π)=1 (road 3).

    Trick: (I - Pᵀ)π = 0 is singular (any scaling works). Adding the all-ones
    matrix J folds in the normalisation: Jπ = (sum π)·ones, so solving
    (I - Pᵀ + J)π = ones forces sum(π) = 1.
    """
    n = P.shape[0]
    A = np.eye(n) - P.T + np.ones((n, n))
    return np.linalg.solve(A, np.ones(n))


def mean_first_passage(P: np.ndarray, target: int) -> np.ndarray:
    """Expected steps to first reach `target` from each state.

    First-step analysis: h_i = 1 + Σ_j P_ij h_j (j ≠ target), h_target = 0.
    Solve the linear system over the non-target states.
    """
    n = P.shape[0]
    others = [i for i in range(n) if i != target]
    Q = P[np.ix_(others, others)]  # transitions among non-target states
    h_others = np.linalg.solve(np.eye(len(others)) - Q, np.ones(len(others)))
    h = np.zeros(n)
    h[others] = h_others
    return h


def spell_lengths(hist: np.ndarray, state: int) -> list[int]:
    """(b) Lengths of unbroken runs of `state`. Any other state ends the run.

    The clean version: flag and counter as SEPARATE concepts.
    (See notes/LORE.md for the sentinel bug this replaces.)
    """
    spells, d, in_spell = [], 0, False
    for s in hist:
        if s == state:
            in_spell = True
            d += 1
        elif in_spell:
            spells.append(d)
            in_spell, d = False, 0
    return spells


def storm_lengths(hist: np.ndarray, storm_state: int = 2, calm_state: int = 0) -> list[int]:
    """(a) First-passage version: from each first entry into `storm_state` until
    the next arrival at `calm_state`. Trending days mid-storm count."""
    storms, d, in_storm = [], 0, False
    for s in hist:
        if s == storm_state:
            in_storm = True
            d += 1
        elif in_storm:
            if s == calm_state:
                storms.append(d)
                in_storm, d = False, 0
            else:
                d += 1
    return storms


def volatile_days_per_excursion(
    hist: np.ndarray, calm_state: int = 0, count_state: int = 2
) -> list[int]:
    """(c) Within each excursion away from `calm_state` and back, how many days
    were spent in `count_state`.

    THIS is where a separate `in_spell` flag is genuinely load-bearing. The
    trigger that OPENS an excursion (any step away from Quiet) is not the same
    as the thing being COUNTED (Volatile days only), so the counter can sit at
    zero while an excursion is truly open — a purely Trending excursion has zero
    Volatile days yet is still a real excursion. Collapsing the two into one
    variable is exactly the sentinel bug in notes/LORE.md.
    """
    excursions, d, in_excursion = [], 0, False
    for s in hist:
        if s == calm_state:
            if in_excursion:  # close it — may legitimately hold zero
                excursions.append(d)
                in_excursion, d = False, 0
        else:
            in_excursion = True
            if s == count_state:
                d += 1
    return excursions


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    hist = simulate(T, 200_000, rng=rng)

    pi_sim = empirical_distribution(hist, 3)
    pi_pow = stationary_by_power(T)
    pi_solve = stationary_by_solve(T)

    print("π three ways (simulate / power / solve):")
    print(" ", pi_sim.round(4), pi_pow.round(4), pi_solve.round(4))

    h = mean_first_passage(T, target=0)
    print("mean first passage to Quiet:", h.round(3), "(theory: h_V = 20/3 = 6.667)")

    spell = round(np.mean(spell_lengths(hist, 2)), 3)
    print("mean volatile spell:", spell, "(theory: 1/0.4 = 2.5)")
    print("mean storm (V until Q):", round(np.mean(storm_lengths(hist)), 3), "(theory: 6.667)")
    print("volatile days per excursion:", round(np.mean(volatile_days_per_excursion(hist)), 3))
