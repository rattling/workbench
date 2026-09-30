# archive

Parked work. Nothing here is maintained, linted or tested — it is excluded from `make gate`.
Kept because it was useful once and may be again, not because it is current.

Nothing has been edited on the way in; these are the files as they were.

| Path | What it is | Why it's parked |
|---|---|---|
| `powell_sdm_lab/` | Powell-style sequential decision making — inventory environment, two policies, trace-first comparison | A different thread (decisions under uncertainty, not probability models). Genuinely useful; likely to come back for ch.5+ or an RL detour. |
| `toy_world_model/` | Learn 1D dynamics from data, recover the equation symbolically with PySR | Standalone experiment. `FINDINGS.md` has the results. Needs `uv sync --group archive` (torch + PySR/Julia). |
| `p1-randomness/` | Drunken-walker labs (k1a/b/c) | Superseded by the notebook's random-walk treatment, which is where the recurrence/transience work actually happened. |
| `first-pass/bunker_price_regimes.py` | The original hand-written regime script | Superseded by `projects/stochastics/prob_models/regime_chain.py`, which took its narrative and its three spell definitions. Kept for the inverse-CDF sampling walkthrough (`np.searchsorted` on a cumsum), which the library version doesn't use. |
| `maths-notes/` | Stage-by-stage syllabus documents and speculative learning paths (physics, biology, complex systems, project ideas) | **The method that didn't work.** Time-boxed curricula with "expected time: 10–20 hours" and "search keywords". Reading-first was tried for two months and killed the thread — see `projects/stochastics/CHARTER.md`. Kept as a monument, not a plan. |
| `scripts/` | `setup-repo.sh` plus generators for apps, "rubes" and web packages | All assume the old `py/packages/*/*` uv workspace. `setup-repo.sh` would actively overwrite the current `pyproject.toml` — **do not run it.** Setup is now just `uv sync`. |

What survived the triage instead of landing here: `projects/stochastics/notes/patterns/` and `…/worked/` — the
recurrence cheat-sheet, canonical problems, and six solved problems (gambler's ruin, HHH/HTH
runs, stopping times). Those are tools reached for mid-build rather than plans to follow, which
is exactly the line the triage drew.
