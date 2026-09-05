"""Bunker-price regime model — a 3-state Markov chain.

Challenge
---------
Bunker fuel prices don't move the same way all the time; they drift between
qualitatively different *regimes*. Model this as a Markov chain with three
states:

    0  Quiet     — prices barely move
    1  Trending  — a sustained directional drift
    2  Volatile  — large, erratic swings

Each step the market jumps to the next regime according to the row of the
transition matrix ``t`` for the current state (each row sums to 1):

                 -> Quiet  Trending  Volatile
    from Quiet    [  0.90     0.08      0.02  ]
    from Trending [  0.20     0.70      0.10  ]
    from Volatile [  0.10     0.30      0.60  ]

The chain is "sticky": every regime most likely stays put (heavy diagonal), so
the market lingers before switching — the clustering you see in real price
series (quiet stretches, trending runs, bursts of volatility).

Questions to answer by simulation
    1. Long-run mix: what fraction of time does the market spend in each
       regime? (the stationary distribution)
    2. How long do turbulent spells last, under three definitions:
       a. storm — from the onset of Volatility until the market calms to Quiet,
          tolerating Trending dips in between;
       b. pure volatility — an unbroken run of Volatile days;
       c. Volatile days per excursion — within each departure from Quiet and
          back, how many days were actually Volatile.

Approach: run the chain for N steps, record the regime at every step, then read
both answers straight off the recorded history.
"""

import random

import numpy as np

labels = ["Quiet", "Trending", "Volatile"]

# Transition matrix. Row s = probabilities of moving FROM regime s to each
# regime on the next step; each row sums to 1. The heavy diagonal (0.9/0.7/0.6)
# is what makes regimes sticky, so runs of the same state are common.
t = [[0.9, 0.08, 0.02], [0.2, 0.7, 0.1], [0.1, 0.3, 0.6]]

N = 100000  # steps to simulate; large N -> empirical stats converge to the truth
hist = []  # regime visited at each step, in order

# Start in a random regime — the starting point washes out over a long run.
s = random.choice([0, 1, 2])
for n in range(N):
    # Sample the next regime by inverse-CDF sampling:
    #   cumsum(t[s]) turns this row's probabilities into bucket edges on [0, 1),
    #   e.g. Quiet's row -> [0.9, 0.98, 1.0]. A uniform random() is a dart thrown
    #   at that line; searchsorted finds which bucket (regime) it lands in using
    #   binary search. side="right" keeps the strict "r < edge" boundary rule.
    s = np.searchsorted(np.cumsum(t[s]), random.random(), side="right")
    hist.append(s)

h = np.asarray(hist)

# Q1 — long-run mix: how many times each regime was visited. Dividing count by N
# gives the empirical stationary distribution.
val, count = np.unique(h, return_counts=True)
print(val, count)

# Q2a — average "storm" length: from the first Volatile (2) step until the
# market next calms to Quiet (0). A storm may dip in and out of Volatile and
# Trending along the way; only a return to Quiet ends it.
#
# No in_spell flag needed: a storm can only open on a Volatile step, which also
# increments d, so d > 0 already means "a storm is open" — d doubles as counter
# and flag.
#   - Volatile (2)             -> open/extend the storm (d += 1)
#   - storm open, Trending (1) -> storm continues (d += 1)
#   - storm open, Quiet (0)    -> storm over: record d, reset (the closing Quiet
#                                 step itself is not counted)
#   - d == 0                   -> no storm open; ignore quiet/trending steps
vp, d = [], 0
for n in hist:
    if n == 2:
        d += 1
    elif d:
        if n == 0:
            vp.append(d)
            d = 0
        else:
            d += 1
print("Stormy period average length")

print(sum(vp) / len(vp))

# Q2b — average "pure volatility" run: the length of an unbroken streak of
# Volatile (2) steps. Here *any* non-Volatile step (Quiet OR Trending) ends the
# run, so this counts only back-to-back volatility — a stricter notion than the
# storm above, which tolerates Trending dips. Same trick as Q2a: the run only
# opens on a Volatile step (d += 1), so d > 0 is the flag; no in_spell needed.
vp, d = [], 0
for n in hist:
    if n == 2:
        d += 1
    elif d:
        vp.append(d)
        d = 0

print("Very stormy period average length (pure volatility)")

print(sum(vp) / len(vp))

# Q2c — average number of Volatile days per "excursion" away from Quiet. A period
# runs from leaving Quiet until returning to it; within it we count only the
# Volatile days. THIS is where a separate in_spell flag is genuinely needed: the
# trigger that opens a period (a step to Trending *or* Volatile) is not the same
# as the thing we count (Volatile days only), so d can sit at 0 while a period is
# truly open — a purely Trending excursion has zero Volatile days yet is still a
# real period. So d > 0 can no longer stand in for "period open".
vp, d, in_spell = [], 0, False
for n in hist:
    if n == 0:  # Quiet -> close the period if one was open (may hold 0 volatile days)
        if in_spell:
            vp.append(d)
            d = 0
            in_spell = False
    else:  # Trending or Volatile -> away from Quiet, so a period is open
        in_spell = True
        if n == 2:
            d += 1  # count only the Volatile days

print("Average volatile days per excursion away from Quiet")

print(sum(vp) / len(vp))

# Theory tripwire for sim
pi = np.linalg.solve((np.eye(3) - np.array(t).T + 1)[:, :], np.ones(3))  # or use null-space
print(pi)
