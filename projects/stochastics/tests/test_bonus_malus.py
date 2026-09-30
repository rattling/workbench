"""Tripwires for the Bonus-Malus ladder.

The whole apparatus exists to produce one business number: the average premium
per policyholder. At λ=1 that number is €477.34, off a stationary distribution
of (0.0707, 0.1214, 0.2594, 0.5484).

The split that took three weeks to see (notes/LORE.md):
    NATURE  — claims per year ~ Poisson(λ). Estimated, falsifiable.
    POSITED — the rule s(i, k). The company's design choice.
P is manufactured from the two; it is not itself a primitive.
"""

import numpy as np
import pytest

from projects.stochastics.prob_models.bonus_malus import (
    N_STATES,
    PREMIUMS,
    average_premium,
    build_matrix,
    rule,
    simulate,
    stationary,
)

# --- the posited rule, checked by hand ---------------------------------------


def test_rule_is_slow_up_fast_down():
    """Zero claims drops you one rung (floored); k claims raise you k (capped)."""
    assert rule(0, 0) == 0  # already on the best rung, stays
    assert rule(2, 0) == 1  # a clean year is worth exactly one rung
    assert rule(1, 2) == 3  # two claims jump two rungs
    assert rule(3, 1) == 3  # already worst, cannot get worse
    assert rule(0, 9) == 3  # capped, not wrapped


# --- P is manufactured, and must still be a stochastic matrix ----------------


def test_every_row_sums_to_one():
    """If a k goes missing from the dummy-variable loop, mass leaks here."""
    P = build_matrix(lam=1.0)
    assert np.allclose(P.sum(axis=1), 1.0)
    assert (P >= 0).all()


def test_truncating_the_claim_count_loop_does_not_move_the_answer():
    """k_max=60 truncates an infinite sum; the tail must be negligible."""
    assert build_matrix(1.0, k_max=25) == pytest.approx(build_matrix(1.0, k_max=150), abs=1e-12)


def test_poisson_pmf_overflows_past_k_equals_170():
    """Known limitation, recorded rather than hidden.

    `poisson_pmf` computes lam**k / factorial(k) naively, and factorial(171)
    exceeds the largest float. So k_max is capped at 170 — comfortably above
    the default 60, but a landmine if anyone raises it. The fix, if it ever
    matters, is the ratio recursion already noted in notes/LORE.md for
    comb(2n, n): step p_k = p_{k-1} * lam / k instead of forming the factorial.
    """
    build_matrix(1.0, k_max=171)  # tops out at k=170 — fine
    with pytest.raises(OverflowError):
        build_matrix(1.0, k_max=172)  # reaches k=171


# --- the stationary distribution and the money -------------------------------


def test_stationary_is_a_fixed_point():
    P = build_matrix(1.0)
    pi = stationary(P)
    assert np.allclose(pi @ P, pi)
    assert pi.sum() == pytest.approx(1.0)


def test_stationary_matches_hand_derived_values():
    pi = stationary(build_matrix(1.0))
    assert pi == pytest.approx([0.0707, 0.1214, 0.2594, 0.5484], abs=1e-4)


def test_average_premium_at_lambda_one():
    assert average_premium(1.0) == pytest.approx(477.34, abs=0.01)


def test_over_half_of_policyholders_sit_on_the_worst_rung():
    """The ladder is slow-up fast-down BY DESIGN — at λ=1 the mass piles at the top."""
    assert stationary(build_matrix(1.0))[N_STATES - 1] > 0.5


def test_simulation_agrees_with_the_linear_solve():
    hist = simulate(1.0, 200_000, rng=np.random.default_rng(1))
    pi_sim = np.bincount(hist, minlength=N_STATES) / len(hist)
    assert pi_sim == pytest.approx(stationary(build_matrix(1.0)), abs=5e-3)


# --- structural limits, derived without touching the code --------------------


def test_no_claims_collapses_everyone_to_the_cheapest_rung():
    """As λ -> 0 nobody ever claims, so all mass slides to state 0 and the
    average premium must approach the cheapest premium."""
    pi = stationary(build_matrix(1e-6))
    assert pi[0] == pytest.approx(1.0, abs=1e-4)
    assert average_premium(1e-6) == pytest.approx(PREMIUMS[0], abs=0.01)


def test_premium_rises_monotonically_with_claim_rate():
    lams = [0.1, 0.3, 0.5, 1.0, 2.0, 5.0]
    premiums = [average_premium(x) for x in lams]
    assert premiums == sorted(premiums)
    # λ=5: P(clean year) = e^-5 ≈ 0.007, so almost everyone is pinned at the
    # worst rung — but not quite, hence 598.6 rather than a clean 600.
    assert premiums[-1] == pytest.approx(598.65, abs=0.05)
