# Reading Roadmap: Fluency in Stochastic Modelling

## Overview: Three Layers

Stochastic modelling rests on three interdependent layers:

1. **Symbol manipulation** — fluency with algebra, functions, recurrences
2. **Probability reasoning** — distributions, expectation, conditional probability
3. **Stochastic modelling** — systems that evolve randomly over time

Most frustration at early stages comes from layer 1 being rusty. Once layer 1 is solid, layers 2 and 3 progress much faster.

---

## Stage 0 — Algebra Foundations

**Goal:** eliminate symbolic friction

**Primary book:**
- **Serge Lang — Basic Mathematics** — clean rebuild of algebra and functions

**Optional supplement:**
- **Gelfand — Algebra** — elegant, problem-driven approach

**Outcome:** fluency with polynomials, exponentials/logs, functions, sequences, and simple recurrences

---

## Stage 1 — Mathematical Problem-Solving

**Goal:** build pattern recognition instincts

**Book:**
- **Paul Zeitz — The Art and Craft of Problem Solving**

**Skills developed:** structural thinking, algebraic manipulation, recurrence intuition, functional equations

**Why it matters:** makes later stochastic work feel intuitive rather than procedural

---

## Stage 2 — Discrete Mathematics Toolbox

**Goal:** master the theoretical foundation for probability and stochastic processes

**Book:**
- **Concrete Mathematics — Graham, Knuth, Patashnik** (focus on: sums, recurrences, finite differences, generating functions)

**Why it matters:** explains why patterns like "constant second difference → quadratic solution" work. This is the technical backbone for recognizing solution types in stochastic recurrences.

---

## Stage 3 — Probability Foundations

**Goal:** formal probability thinking with emphasis on modelling

**Primary book:**
- **Blitzstein & Hwang — Introduction to Probability** — teaches probability through modelling problems

**What's covered:**
- conditional probability and expectation
- discrete Markov chains and transition matrices
- random walks and absorbing states
- hitting probabilities and stationary distributions
- classic problems: gamblers' ruin, pattern waiting times, board games

**Strong alternative (free online):**
- **Grinstead & Snell — Introduction to Probability** — excellent clarity; chapters on random walks and absorbing chains particularly strong

---

## Stage 4 — Stochastic Processes and Markov Chains

**Goal:** model systems evolving over time; deepen Markov chain understanding

**Primary book:**
- **Sheldon Ross — Introduction to Probability Models** — applies Markov chains to real systems: queues, inventories, reliability, population dynamics. Widely used in engineering and operations research.

**More theoretical alternative:**
- **Norris — Markov Chains** — covers irreducibility, recurrence/transience, detailed long-run behavior

**Typical progression:**
Blitzstein/Grinstead → Ross → (optionally) Norris

---

## Stage 5 — Applied Stochastic Modelling

**Goal:** build domain-specific models

Choose based on application area:

| Domain | Recommended Book |
|--------|------------------|
| Operations / Queueing | Allen — Probability, Statistics and Queueing Theory |
| Statistical Physics | Kardar — Statistical Physics of Particles |
| Finance | Shreve — Stochastic Calculus for Finance |
| Reinforcement Learning | Sutton & Barto — Reinforcement Learning |

---

## Complete Learning Path

```
Stage 0 (Algebra)
        ↓
     Lang
        ↓
Stage 1 (Problem-Solving)
        ↓
     Zeitz
        ↓
Stage 2 (Discrete Math)
        ↓
  Concrete Mathematics
        ↓
Stage 3 (Probability)
        ↓
  Blitzstein or Grinstead
        ↓
Stage 4 (Stochastic Processes)
        ↓
     Ross (± Norris)
        ↓
Stage 5 (Applications)
        ↓
  Domain-specific book
```

---

## What You Can Do By Each Stage

| Stage | Core Competencies |
|-------|-------------------|
| After Stage 0 | Manipulate algebraic expressions; work with functions and sequences |
| After Stage 1 | See structural patterns; choose solution approaches strategically |
| After Stage 2 | Solve recurrences; recognize when constant second differences imply quadratic solutions |
| After Stage 3 | Set up Markov chains; solve for hitting probabilities and absorption times; compute stationary distributions |
| After Stage 4 | Model real systems with Markov chains; understand queues, transient vs. long-run behavior |
| After Stage 5 | Build models in your domain; make stochastic predictions and decisions |

---

## Markov Chains: The Central Structure

Once you reach stage 4, you'll notice that roughly **half of applied stochastic modelling is just Markov chains**.

They are the central mathematical structure behind:

- reliability and failure analysis
- queueing systems
- random walks and diffusion
- pattern matching in coin tosses
- population dynamics
- financial options pricing

**The problems you've already solved** (coin pattern waiting times, gambler's ruin, hitting probabilities) are classic Markov chain exercises. When you open Ross or Blitzstein, you'll recognize the same recurrence structures.

---

## Condensed Path (80/20 Rule)

If you're short on time, the essential subset is:

1. **Concrete Mathematics** — chapters 6–7 on recurrences and sums
2. **Blitzstein & Hwang** — chapters on Markov chains and random walks
3. **Ross** — chapters on queueing and continuous-time Markov chains

This covers ~80% of the modelling power used in applications, skipping pure theory and advanced topics.

---

## Notes on Skipping

- **Algebra foundations** should not be skipped if you struggle with symbol manipulation
- **Problem-solving** can be condensed if you already work through puzzles regularly
- Most of **Concrete Mathematics** beyond recurrences can be deferred
- **Grinstead & Snell** can fully replace Blitzstein if free access is important
- **Norris** is optional; only needed if you want rigorous asymptotic theory
