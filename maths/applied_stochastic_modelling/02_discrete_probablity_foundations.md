# Step 2 — Discrete Probability for Stochastic Modelling

## Purpose
This stage builds the probabilistic intuition needed before formal Markov chain theory.
It focuses on modelling small stochastic systems using **first‑step reasoning and recurrences**.

Expected time: 10–20 hours.

---

## Core Ideas

Key modelling technique:

1. Define the quantity of interest
2. Condition on the next step
3. Write a recurrence relation
4. Solve using algebra tools from Step 1
5. Apply boundary conditions

---

## Section 1 — Conditional Probability Refresh

Concepts

- conditional probability
- law of total probability
- independence

Exercises

- Compute conditional probabilities for simple coin experiments
- Verify the law of total probability with two events

Search keywords

- conditional probability basics
- law of total probability examples

---

## Section 2 — First‑Step Analysis

Concept

Instead of analysing the full stochastic process, condition on the **next step**.

Example pattern

E_i = 1 + 1/2 E_{i+1} + 1/2 E_{i-1}

Exercises

- Write first‑step equations for simple random walks
- Derive recurrence relations for hitting probabilities

Search keywords

- first step analysis probability
- conditioning on next step random walk

---

## Section 3 — Random Walks

Concept

At each step:

+1 with probability p
−1 with probability 1−p

Topics

- symmetric random walk
- biased random walk
- drift

Exercises

- Simulate a short random walk
- Compute probability of reaching +2 in two steps

Search keywords

- random walk probability model
- biased random walk explanation

---

## Section 4 — Gambler’s Ruin

Model

States: 0..N
Boundaries: 0 (ruin), N (success)

Key problems

- probability of hitting N before 0
- expected time to absorption

Exercises

- derive recurrence for fair case
- derive recurrence for biased case

Search keywords

- gambler's ruin problem explanation
- hitting probability random walk

---

## Section 5 — Stopping Times

Concept

Random time until an event occurs.

Examples

- time until first head
- time until two heads in a row
- time until hitting boundary

Exercises

- expected time for one head
- expected time for two heads in a row

Search keywords

- stopping time probability
- expected waiting time coin flips

---

## Section 6 — Small Markov Chains

Concept

Finite states with transition probabilities.

Exercises

- build Markov chain for HTH pattern detection
- compute absorption probability

Search keywords

- absorbing Markov chain basics
- markov chain coin toss patterns

---

## Outcome

You should now be comfortable:

- writing first‑step equations
- modelling simple stochastic systems
- solving probability recurrences