# State of play — stochastics thread

*Live state. Update at every close-out. Method and invariants live in
[`CHARTER.md`](CHARTER.md); bugs live in [`notes/LORE.md`](notes/LORE.md).*

**Last updated:** 2026-09-05

## Where the chapter stands

Ross ch. 4 (Markov chains) — most of the way through conceptually, **none of it examined yet.**

| Section | Status |
|---|---|
| 4.1 definitions, Markov property, state augmentation ("the dimensionality cheat") | ✅ |
| 4.2 Chapman–Kolmogorov — derived by hand at n=m=1, matrix-power meaning, scalar trap | ✅ |
| 4.3 classification — accessible / communicate / classes, recurrent = certain RETURN, transient = geometric visit count, census test Σ Pⁿᵢᵢ, drunk walk 1D/2D recurrent vs 3D transient | ✅ |
| 4.4 limiting probabilities | ⬜ not read — but already computed empirically (63.4/26.8/9.9), so the section will be confirmation, not new material |
| **Ross exercises** | ⬜ **none attempted. This is the open audit.** |

Worked cold and now under test: the regime chain, π three ways, mean first passage (h_V = 20/3),
spell lengths (geometric, 2.5), Bonus-Malus end to end with the nature-vs-posited split.

## Notebooks

| Notebook | Covers | Ross | Status |
|---|---|---|---|
| `01-regimes-and-markov-chains` | regime sim, π three ways, first passage, spells, CK, classification, Bonus-Malus | 4.1–4.3 (+4.4 preview) | scaffolded, runs clean — **✍️ prose cells still to backfill** |
| `02-hidden-regimes` | HMM on real price data; how many regimes reality supports | Hamilton (off-book) | next |
| `03-ruin-and-absorption` | gambler's ruin, absorbing barriers, blowup times | 4.5-ish | queued |
| `04-arrival-streams` | Poisson processes from memoryless gaps; merge / thin | ch. 5 | queued |
| `05-bonus-malus-premium-machine` | full pricing study, λ sensitivity | 4.1 revisited | queued |

## Next actions, in order

1. **Ross ch.4 exercises, cold.** LLM-free, at the open of the next session. Pencil the problem
   numbers into notebook 01 §9 first — the slots are already there (1 drill, 2 modelling, 1
   classification). Post-mortems only after a genuine attempt.
2. **Backfill notebook 01's ✍️ cells** in own words. This *is* the revision — nobody else writes
   these.
3. **Notebook 02 — the HMM pilot.** Real price data (Brent to build, VLSFO when sourced),
   `hmmlearn`, 2-vs-3 regimes by BIC, regime ribbon against desk memory (does it flag Mar-2020?
   2022?), fitted persistence vs the invented 0.9/0.7/0.6. Doubles as the "timing intelligence"
   artifact for the commercial thread.
4. Then 03 / 04 / 05 as queued above.

## Open questions

- **`poisson_pmf` overflow cliff** (found 2026-09-05 while writing tripwires): it forms
  `lam**k / factorial(k)` directly, so `k_max > 171` raises `OverflowError`. Harmless at the
  default 60, and `test_poisson_pmf_overflows_past_k_equals_170` pins the limit so it can't
  surprise anyone. Fix it with the ratio recursion (already in LORE for `comb(2n,n)`) or leave
  it — a decision, not a bug to be silently patched.
- Notebook 01 §9's Ross problem numbers depend on which edition is to hand. Not yet filled in.

## Recently done

**2026-09-30 — projects layout.** The workbench took a second tenant (bioplastics), so the
thread moved from `src/labs/`, `tests/`, `notebooks/` and `notes/` into `projects/stochastics/`.
Imports are now `projects.stochastics.prob_models`. Nothing inside the thread changed.

**2026-09-05 — repo restructure.** Flattened `py/packages/labs/src/labs/` to `src/labs/`; killed
the uv workspace (four `pyproject.toml`s that declared no dependencies between them). Merged the
`stochastics-notebooks` zip into the tree — notebook, `regime_chain`, `bonus_malus`, `LORE.md` —
and reconciled the two copies of the regime model into one. Replaced the smoke tests with 24
real tripwires against hand-derived theory. Parked Powell SDM, the toy world model, the drunken
walkers, and the old syllabus notes in `archive/`. Wrote the charter and `AGENTS.md`.
