# HTH vs HHH: Pattern Race

Find the probability that we see HTH before HHH in a sequence of coin tosses.

## 1. Setup

### Define states and transition probabilities

States represent the progress toward each pattern:
- $S_0$ : no progress toward either pattern
- $S_H$ : seen one H (progress toward both)
- $S_{HH}$ : seen HH (progress toward HHH only)
- $S_{HT}$ : seen HT (progress toward HTH only)
- HHH : reached HHH first (absorbing state)
- HTH : reached HTH first (absorbing state)

### Set up the problem

Let $P_i$ be the probability of reaching HTH before HHH starting from state $i$.

We want to find $P_0$.

### Set up equations based on transitions

From $S_0$:

> $S_0 \xrightarrow{H(1/2)} S_H$
>
> $S_0 \xrightarrow{T(1/2)} S_0$
>
> $P_0 = \frac{1}{2}P_H + \frac{1}{2}P_0$

---

From $S_H$:

> $S_H \xrightarrow{H(1/2)} S_{HH}$
>
> $S_H \xrightarrow{T(1/2)} S_{HT}$
>
> $P_H = \frac{1}{2}P_{HH} + \frac{1}{2}P_{HT}$

---

From $S_{HH}$:

> $S_{HH} \xrightarrow{H(1/2)} \text{HHH (lose)}$
>
> $S_{HH} \xrightarrow{T(1/2)} S_{HT}$
>
> $P_{HH} = \frac{1}{2} \cdot 0 + \frac{1}{2}P_{HT}$

---

From $S_{HT}$:

> $S_{HT} \xrightarrow{H(1/2)} \text{HTH (win)}$
>
> $S_{HT} \xrightarrow{T(1/2)} S_0$
>
> $P_{HT} = \frac{1}{2} \cdot 1 + \frac{1}{2}P_0$

## 2. Solve the system of equations

From $P_{HT}$:

$P_{HT} = \frac{1}{2} + \frac{1}{2}P_0 \quad (1)$

From $P_{HH}$:

$P_{HH} = \frac{1}{2}P_{HT} \quad (2)$

From $P_H$:

$P_H = \frac{1}{2}P_{HH} + \frac{1}{2}P_{HT}$

Substituting (2):

$P_H = \frac{1}{2} \cdot \frac{1}{2}P_{HT} + \frac{1}{2}P_{HT} = \frac{1}{4}P_{HT} + \frac{1}{2}P_{HT} = \frac{3}{4}P_{HT} \quad (3)$

From $P_0$:

$P_0 = \frac{1}{2}P_H + \frac{1}{2}P_0$

$\Rightarrow \frac{1}{2}P_0 = \frac{1}{2}P_H$

$\Rightarrow P_0 = P_H \quad (4)$

Substituting (3) into (4):

$P_0 = \frac{3}{4}P_{HT}$

Substituting (1):

$P_0 = \frac{3}{4}\left(\frac{1}{2} + \frac{1}{2}P_0\right)$

$P_0 = \frac{3}{8} + \frac{3}{8}P_0$

$P_0 - \frac{3}{8}P_0 = \frac{3}{8}$

$\frac{5}{8}P_0 = \frac{3}{8}$

$P_0 = \frac{3}{5}$

Thus, the probability of seeing HTH before HHH is $\boxed{\frac{3}{5}}$.
