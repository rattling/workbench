"""Tripwires for the regime chain — theory vs code.

Each invariant gets its own named test. The closed forms asserted here were
derived by hand, independently of the code under test; nothing here checks a
result against its own arithmetic.

Anchor numbers (from the hand derivations):
    π   = (0.6338, 0.2676, 0.0986)
    h_V = 20/3 ≈ 6.667      mean first passage Volatile -> Quiet
    mean pure-Volatile spell = 1/(1 - 0.6) = 2.5   (geometric)
"""

import numpy as np
import pytest

from labs.prob_models.regime_chain import (
    LABELS,
    T,
    empirical_distribution,
    mean_first_passage,
    simulate,
    spell_lengths,
    stationary_by_power,
    stationary_by_solve,
    storm_lengths,
    volatile_days_per_excursion,
)

QUIET, TRENDING, VOLATILE = 0, 1, 2


@pytest.fixture(scope="module")
def hist():
    """One long path, fixed seed, shared across the statistical tests."""
    return simulate(T, 200_000, rng=np.random.default_rng(42))


# --- the transition matrix itself -------------------------------------------


def test_rows_are_probability_distributions():
    assert np.allclose(T.sum(axis=1), 1.0)
    assert (T >= 0).all()
    assert T.shape == (len(LABELS), len(LABELS))


# --- π, three independent roads ---------------------------------------------


def test_stationary_is_a_fixed_point_of_the_matrix():
    """The definition itself: πP = π, and π sums to 1.

    Independent of how π was obtained — this is what "stationary" means.
    """
    pi = stationary_by_solve(T)
    assert np.allclose(pi @ T, pi)
    assert pi.sum() == pytest.approx(1.0)


def test_stationary_matches_hand_derived_values():
    assert stationary_by_solve(T) == pytest.approx([0.633803, 0.267606, 0.098592], abs=1e-6)


def test_solve_and_matrix_power_agree():
    """Road 2 (Chapman-Kolmogorov / convergence) meets road 3 (linear solve)."""
    assert stationary_by_power(T, n=200) == pytest.approx(stationary_by_solve(T), abs=1e-9)


def test_simulation_agrees_with_solve(hist):
    """Road 1 (simulate) meets road 3. Loose tolerance: this is Monte Carlo."""
    assert empirical_distribution(hist, 3) == pytest.approx(stationary_by_solve(T), abs=5e-3)


def test_origin_washes_out():
    """Starting state is forgotten: every row of P^n converges to the same π."""
    Pn = np.linalg.matrix_power(T, 200)
    assert np.allclose(Pn, Pn[0], atol=1e-9)


# --- first passage -----------------------------------------------------------


def test_mean_first_passage_to_quiet_is_20_over_3():
    """h_V = 20/3 exactly; h_Q = 0 by definition."""
    h = mean_first_passage(T, target=QUIET)
    assert h[QUIET] == 0.0
    assert h[VOLATILE] == pytest.approx(20 / 3)
    assert h[TRENDING] == pytest.approx(50 / 9)


def test_simulated_storm_length_matches_first_passage(hist):
    """A storm IS the first passage V -> Q, so its mean must land on h_V."""
    assert np.mean(storm_lengths(hist)) == pytest.approx(20 / 3, abs=0.1)


# --- spells ------------------------------------------------------------------


def test_pure_volatile_spell_is_geometric(hist):
    """Unbroken runs of V leave with prob 1 - P[V,V], so mean = 1/0.4 = 2.5."""
    assert np.mean(spell_lengths(hist, VOLATILE)) == pytest.approx(2.5, abs=0.05)


def test_three_spell_definitions_are_ordered(hist):
    """Storms tolerate Trending dips, so they cannot be shorter than pure runs."""
    assert np.mean(storm_lengths(hist)) > np.mean(spell_lengths(hist, VOLATILE))


# --- the sentinel bug: a named regression test -------------------------------
#
# hist below, by eye:
#   idx    0  1  2  3  4  5  6  7  8  9 10 11
#   state  Q  T  T  Q  V  V  T  V  Q  T  V  Q
#
# excursions away from Quiet:  [T,T]  [V,V,T,V]  [T,V]
# volatile days in each:          0        3        1
HAND_CHECKED = np.array([0, 1, 1, 0, 2, 2, 1, 2, 0, 1, 2, 0])


def test_purely_trending_excursion_records_zero_volatile_days():
    """THE sentinel-bug regression (see notes/LORE.md).

    An excursion that never reaches Volatile is still a real excursion and must
    be recorded with a count of zero. Collapsing the "excursion is open" flag
    into the "volatile days" counter loses it entirely — that leading 0 is the
    whole test.
    """
    assert volatile_days_per_excursion(HAND_CHECKED) == [0, 3, 1]


def test_spell_and_storm_on_the_hand_checked_history():
    assert spell_lengths(HAND_CHECKED, VOLATILE) == [2, 1, 1]
    assert storm_lengths(HAND_CHECKED) == [4, 1]


def test_open_spell_at_end_of_history_is_not_counted():
    """A right-censored spell has no observed end; averaging it in would bias
    the mean downward. Dropping it is deliberate, not an oversight."""
    assert spell_lengths(np.array([0, 2, 2]), VOLATILE) == []
    assert storm_lengths(np.array([0, 2, 1])) == []
