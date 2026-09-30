# Coin Toss Runs

Find the expected number of tosses to get three heads in a row (HHH).

## 1. Setup 

### Define states and expected values

$S_0, S_1, S_2, S_3$ are the states of the Markov chain, where $S_i$ represents the state of having $i$ consecutive heads.

> $E_0$ : expected number of tosses to reach $S_3$ starting from $S_0$  
> $E_1$ : expected number of tosses to reach $S_3$ starting from $S_1$  
> $E_2$ : expected number of tosses to reach $S_3$ starting from $S_2$  

### Set up equations based on transitions

From $S_0$:

> $S_0 \xrightarrow{H(1/2)} S_1$
>
> $S_0 \xrightarrow{T(1/2)} S_0$
>
> $E_0 = 1 + \frac{1}{2}E_1 + \frac{1}{2}E_0$

---

From $S_1$:

> $S_1 \xrightarrow{H(1/2)} S_2$
>
> $S_1 \xrightarrow{T(1/2)} S_0$
>
> $E_1 = 1 + \frac{1}{2}E_2 + \frac{1}{2}E_0$  

---

From $S_2$:

> $S_2 \xrightarrow{H(1/2)} S_3$
>
> $S_2 \xrightarrow{T(1/2)} S_0$
>
> $E_2 = 1 + \frac{1}{2}*0 + \frac{1}{2}E_0$  

## 2. Solve the system of equations

From $E_0$:

$E_0 = 1 + \frac{1}{2}E_1 + \frac{1}{2}E_0$

$\Rightarrow \frac{1}{2}E_0 = 1 + \frac{1}{2}E_1$

$\Rightarrow E_0 = 2 + E_1 \quad (1)$

From $E_1$:

$E_1 = 1 + \frac{1}{2}E_2 + \frac{1}{2}E_0$

$\Rightarrow E_1 = 1 + \frac{1}{2}E_2 + \frac{1}{2}(2 + E_1)$

$\Rightarrow E_1 = 1 + \frac{1}{2}E_2 + 1 + \frac{1}{2}E_1$

$\Rightarrow \frac{1}{2}E_1 = 2 + \frac{1}{2}E_2$

$\Rightarrow E_1 = 4 + E_2 \quad (2)$

From $E_2$:

$E_2 = 1 + \frac{1}{2} \cdot 0 + \frac{1}{2}E_0$

$\Rightarrow E_2 = 1 + \frac{1}{2}E_0 \quad (3)$

Substituting (3) into (2):

$E_1 = 4 + 1 + \frac{1}{2}E_0$

$\Rightarrow E_1 = 5 + \frac{1}{2}E_0 \quad (4)$

Substituting (4) into (1):

$E_0 = 2 + 5 + \frac{1}{2}E_0$

$\Rightarrow E_0 = 7 + \frac{1}{2}E_0$

$\Rightarrow \frac{1}{2}E_0 = 7$

$\Rightarrow E_0 = 14$





