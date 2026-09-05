# Stochastic Modelling Project Ideas (Helionyx Lab)

These projects require little or no external data.  
The goal is to **understand real systems driven by randomness** through theory + simulation.

They also align well with the mathematics being learned:

- discrete probability
- Markov chains
- recurrence relations
- Monte Carlo simulation

Each project can be implemented as a small module inside **Helionyx**.

---

# 1. Random Walk → Diffusion

## Core Question
How does microscopic randomness produce smooth macroscopic behaviour?

## Model

A particle moves randomly:

x_{t+1} = x_t + step

step ∈ {−1, +1}

or continuous random steps.

## Experiments

- distribution of positions after n steps  
- variance growth over time  
- hitting probability of boundaries  
- multi-particle diffusion

## Key Result

variance ∝ time

This leads directly to **diffusion and Brownian motion**.

## Scientific Context

Used in:

- molecular motion
- heat diffusion
- option pricing
- particle physics

---

# 2. Percolation (Connectivity Phase Transition)

## Core Question

When does a random system suddenly become connected?

## Model

Grid where each cell is open with probability p:

open with probability p  
closed with probability 1 − p

Check whether a path exists across the grid.

## Experiments

- probability of spanning path  
- cluster size distribution  
- identify critical threshold p_c

## Key Insight

A **phase transition** occurs:

Below threshold → small clusters  
Above threshold → giant connected component

## Scientific Context

Used in:

- porous materials
- network robustness
- forest fire models
- epidemic spread

---

# 3. Epidemic Spread (SIR Model)

## Core Question

When does an infection explode vs die out?

## Model

Individuals transition between states:

S → susceptible  
I → infected  
R → recovered

Transitions:

S → I with probability β  
I → R with probability γ

## Experiments

- outbreak probability  
- epidemic threshold  
- distribution of outbreak sizes

## Key Concept

R₀ (reproduction number)

## Scientific Context

Used in:

- epidemiology
- information spread
- network science

---

# 4. Search Processes

## Core Question

How long does it take to find a target in a random environment?

## Model

Agent performs random walk in space.

Variants:

- pure random walk  
- biased search  
- Lévy flight  

## Experiments

- time to reach target  
- coverage of region  
- efficiency of search strategies

## Scientific Context

Used in:

- animal foraging
- robotics
- molecule binding
- optimisation algorithms

---

# 5. Birth–Death Processes (Population Dynamics)

## Core Question

How do populations evolve under random reproduction and death?

## Model

population_{t+1} =
    population_t
    + births
    − deaths

Births and deaths occur probabilistically.

## Experiments

- extinction probability  
- expected time to extinction  
- long-run population distribution

## Scientific Context

Used in:

- ecology
- evolutionary biology
- queueing systems
- chemical reactions

---

# Core Phenomena These Projects Represent

These five systems capture fundamental stochastic behaviours:

| Phenomenon | Example System |
|-------------|---------------|
| Diffusion | Random Walk |
| Connectivity | Percolation |
| Contagion | Epidemics |
| Search | Exploration Processes |
| Growth / Decay | Birth–Death Models |

Understanding these patterns provides a strong foundation for:

- statistical physics
- complex systems
- stochastic modelling
- reinforcement learning
- operations research

---

# Helionyx Stochastic Lab Concept

Possible module structure:
