# AGENTS.md

## What this is

A personal workbench. Its current and primary tenant is a **stochastics learning thread** —
working through the material of Ross, *Introduction to Probability Models*, by building first and
using the text as an examination layer. Other prototypes are welcome here, but the stochastics
thread sets the conventions.

Read `docs/CHARTER.md` before doing anything substantive. The method is not negotiable and it is
not obvious — text-first was tried and abandoned for good reasons.

## Read order

1. `docs/CHARTER.md` — purpose, success criterion, invariants, scope ladder, anchor numbers
2. `STATE-OF-PLAY.md` — where the thread actually is right now, and what's next
3. `notes/LORE.md` — the bug ledger. **Read this before debugging anything.**
4. `~/repos/ways-of-working/WORKING-CONTRACT.md` — how work is delegated and handed back

## Layout

```
src/labs/<lab>/       the machinery — anything over ~30 lines lives here, not in a notebook
tests/<lab>/          tripwires: hand-derived theory vs the code
notebooks/            the journey. Every claim runs; ✍️ cells are written unaided
notes/                LORE.md (bugs), patterns/ (recurrence shapes), worked/ (solved problems)
docs/                 CHARTER.md and reference
data/                 gitignored except .gitkeep
archive/              parked threads. Not maintained, not linted, not tested.
```

One package, one venv, one `pyproject.toml`. A lab is a subpackage of `labs`, imported as
`from labs.prob_models import ...`. There is no workspace and nothing to register — adding a lab
is `make lab NAME=<name>`.

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
- `archive/` is read-only history. Don't refactor it, lint it, or fold it back in unrevised.

## Gate

```bash
make gate      # ruff check + ruff format --check + pytest
```

Everything must be green before a thread is called done. For the notebook, "green" also means it
executes top to bottom:

```bash
uv run --with nbclient --with jupyter-client python -c "
import nbformat; from nbclient import NotebookClient
nb = nbformat.read('notebooks/01-regimes-and-markov-chains.ipynb', as_version=4)
NotebookClient(nb, timeout=600, resources={'metadata':{'path':'notebooks/'}}).execute()
print('clean')"
```

## Environment

```bash
uv sync                      # everything the live labs need
uv sync --group archive      # + torch and pysr, only for archive/toy_world_model
```
