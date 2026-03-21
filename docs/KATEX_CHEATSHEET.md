# KaTeX Cheat Sheet

A quick reference for writing mathematical expressions using **KaTeX** in Markdown.

---

# 1. Basic Math Modes

## Inline Math

Wrap expressions with single dollar signs.

Example: To write P(X=1), use: $P(X=1)$

## Display Math (Centered)

Use double `$$` on separate lines for centered equations.

```
$$
\pi_{t+1} = \pi_t P
$$
```

Result:
$$\pi_{t+1} = \pi_t P$$

---

# 2. Greek Letters

Common letters: `\alpha`, `\beta`, `\gamma`, `\delta`, `\lambda`, `\pi`, `\theta`, `\sigma`, `\omega`

Examples:
- Type `\alpha` renders as $\alpha$
- Type `\beta` renders as $\beta$
- Type `\gamma` renders as $\gamma$
- Type `\pi_t` renders as $\pi_t$
- Type `\theta` renders as $\theta$

---

# 3. Superscripts and Subscripts

| What To Type | Result |
|---|---|
| x^2 | $x^2$ |
| x_t | $x_t$ |
| x_{t+1} | $x_{t+1}$ |
| P^t | $P^t$ |
| x_i^2 | $x_i^2$ |

---

# 4. Fractions

Type: `\frac{numerator}{denominator}`

Examples:
- Type `\frac{q}{p}` renders as $\frac{q}{p}$
- Type `\frac{x+1}{y-2}` renders as $\frac{x+1}{y-2}$

---

# 5. Square Roots

Type: `\sqrt{x}` or `\sqrt[n]{x}` for nth root

Examples:
- Type `\sqrt{x}` renders as $\sqrt{x}$
- Type `\sqrt{x^2 + y^2}` renders as $\sqrt{x^2 + y^2}$
- Type `\sqrt[3]{27}` renders as $\sqrt[3]{27}$

---

# 6. Matrices

Type:
```
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
```

Result:
$$P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$$

Other styles:
- `pmatrix` (parentheses) renders as $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$
- `bmatrix` (brackets) renders as $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$
- `vmatrix` (vertical bars) renders as $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$

---

# 7. Probability Notation

| Code | Result |
|---|---|
| P(A \mid B) | $P(A \mid B)$ |
| P(X_{t+1}=j \mid X_t=i) | $P(X_{t+1}=j \mid X_t=i)$ |

---

# 8. Expectation

| Code | Result |
|---|---|
| E[X] | $E[X]$ |
| \mathbb{E}[X] | $\mathbb{E}[X]$ |
| \mathbb{E}[X \mid Y] | $\mathbb{E}[X \mid Y]$ |

---

# 9. Summation & Products

| Code | Result |
|---|---|
| \sum_{i=1}^{n} x_i | $\sum_{i=1}^{n} x_i$ |
| \prod_{i=1}^{n} x_i | $\prod_{i=1}^{n} x_i$ |

Display mode (centered):
$$\sum_{i=1}^{n} x_i$$

---

# 10. Integrals

| Code | Result |
|---|---|
| \int_a^b f(x)\,dx | $\int_a^b f(x)\,dx$ |
| \iint_D f(x,y)\,dA | $\iint_D f(x,y)\,dA$ |

---

# 11. Aligned Equations

For step-by-step derivations:

```
\begin{aligned}
x &= y + 2 \\
  &= 3 + 2 \\
  &= 5
\end{aligned}
```

Result:
$$\begin{aligned} x &= y + 2 \\ &= 3 + 2 \\ &= 5 \end{aligned}$$

---

# 12. Vectors

| Code | Result |
|---|---|
| \vec{x} | $\vec{x}$ |
| \mathbf{x} | $\mathbf{x}$ |
| \mathbf{v} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} | $\mathbf{v} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ |

---

# 13. Sets

| Code | Result |
|---|---|
| \{1,2,3\} | $\{1,2,3\}$ |
| S = \{0,1,2,3\} | $S = \{0,1,2,3\}$ |
| A \cup B | $A \cup B$ |
| A \cap B | $A \cap B$ |
| A \subseteq B | $A \subseteq B$ |
| x \in S | $x \in S$ |
| x \notin S | $x \notin S$ |

---

# 14. Markov Chain Notation

**Transition matrix:**
$$P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$$

**State distribution:**
Type `\pi_t = [0.2, 0.8]` renders as $\pi_t = [0.2, 0.8]$

**Evolution:**
Type `\pi_{t+1} = \pi_t P` renders as $\pi_{t+1} = \pi_t P$

**Steady state:**
Type `\pi = \pi P` renders as $\pi = \pi P$

---

# 15. Logical Symbols

| Code | Result |
|---|---|
| A \Rightarrow B | $A \Rightarrow B$ |
| A \Leftarrow B | $A \Leftarrow B$ |
| A \iff B | $A \iff B$ |
| \forall x | $\forall x$ |
| \exists x | $\exists x$ |
| x \neq y | $x \neq y$ |
| x \leq y | $x \leq y$ |
| x \geq y | $x \geq y$ |
| x \approx y | $x \approx y$ |

---

# 16. Limits & Infinity

| Code | Result |
|---|---|
| \lim_{x \to \infty} f(x) | $\lim_{x \to \infty} f(x)$ |
| \lim_{n \to 0} \frac{1}{n} | $\lim_{n \to 0} \frac{1}{n}$ |
| \infty | $\infty$ |

---

# 17. Norms & Absolute Values

| Code | Result |
|---|---|
| \|x\| | $\|x\|$ |
| \|\mathbf{v}\|_2 | $\|\mathbf{v}\|_2$ |
| \|x - y\| | $\|x - y\|$ |

---

# 18. Spacing

Use for better readability:

- Type `\,` for small space: `f(x)\,dx` renders as $f(x)\,dx$
- Type `\quad` for medium space: renders as $a \quad b$
- Type `\qquad` for large space: renders as $a \qquad b$

---

# 19. Quick Reference

| Operation | Code |
|-----------|------|
| Fraction | \frac{a}{b} |
| Subscript | x_i |
| Superscript | x^2 |
| Square root | \sqrt{x} |
| Sum | \sum_{i=1}^{n} |
| Product | \prod_{i=1}^{n} |
| Integral | \int_a^b |
| Infinity | \infty |
| Pi | \pi |
| Alpha | \alpha |

---

# 20. Best Practices

1. **Inline Math:** Use single `$...$` for math within text
2. **Display Math:** Use `$$...$$` on separate lines for standalone equations
3. **Grouping:** Always use braces for multi-char subscripts: `x_{t+1}` not `x_t+1`
4. **Integrals:** Add spacing before dx: `\int f(x)\,dx`
5. **Conditionals:** Use `\mid` for probability, not `|`
6. **Common Mistake:**
   - Wrong: `x_t+1` renders as $x_t+1$
   - Right: `x_{t+1}` renders as $x_{t+1}$

---

# 21. Official Documentation

Full reference: https://katex.org/docs/supported.html

---

**End of cheat sheet.**
