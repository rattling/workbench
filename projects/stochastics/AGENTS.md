# AGENTS.md — stochastics thread

Working through the material of Ross, *Introduction to Probability Models*, by building first and
using the text as an examination layer. Read [`CHARTER.md`](CHARTER.md) before doing anything
substantive. The method is not negotiable and it is not obvious — text-first was tried and
abandoned for good reasons.

## Read order

1. `CHARTER.md` — purpose, success criterion, invariants, scope ladder, anchor numbers
2. `STATE-OF-PLAY.md` — where the thread actually is right now, and what's next
3. `notes/LORE.md` — the bug ledger. **Read this before debugging anything.**

## Layout

```
prob_models/   the machinery — anything over ~30 lines lives here, not in a notebook
tests/         tripwires: hand-derived theory vs the code
notebooks/     the journey. Every claim runs; ✍️ cells are written unaided
notes/         LORE.md (bugs), patterns/ (recurrence shapes), worked/ (solved problems)
```

Import as `from projects.stochastics.prob_models import regime_chain`. A new lab is a sibling
subpackage of `prob_models/`.

## Rules

- **The cord:** three consecutive text-decoding exchanges without running code — stop and build.
  Either party pulls it.
- **Never write the ✍️ prose cells.** Those are retrieval practice; filling them in destroys the
  exercise. Scaffold them, mark them TODO, leave them.
- **Never do the Ross exercises**, or hint at their answers, unless explicitly asked for a
  post-mortem *after* a genuine cold attempt.
- Tripwires assert hand-derived closed forms. Never assert a value the code just produced.
- Wrong guesses are curriculum — when a prediction misses, record the gap rather than silently
  fixing it.
- Surprises go to `notes/LORE.md` as one dated line. Decisions go to the charter, not lore.

## Notebook gate

"Green" for this thread also means notebook 01 executes top to bottom. From the repo root:

```bash
uv run --with nbclient --with jupyter-client python -c "
import nbformat; from nbclient import NotebookClient
p = 'projects/stochastics/notebooks/01-regimes-and-markov-chains.ipynb'
nb = nbformat.read(p, as_version=4)
NotebookClient(nb, timeout=600, kernel_name='workbench',
               resources={'metadata': {'path': 'projects/stochastics/notebooks/'}}).execute()
print('clean')"
```
