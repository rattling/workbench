# AGENTS.md

## What this is

A personal workbench of self-contained research projects. Each project lives in its own folder
under `projects/`, with its own code, notebooks, notes and tests side by side. All projects share
one `pyproject.toml`, one venv and one root package.

**Before working in a project, read its `AGENTS.md` (or `README.md` if it has none).** Project
rules apply inside that project only — the stochastics thread's rules about ✍️ cells and Ross
exercises, for example, don't bind anything else.

| Project | What it is |
|---|---|
| [`projects/stochastics/`](projects/stochastics/AGENTS.md) | Ross, *Introduction to Probability Models*, build-first |
| [`projects/bioplastics/`](projects/bioplastics/README.md) | Researching and modelling biodegradable plastics |

Also read `~/repos/ways-of-working/WORKING-CONTRACT.md` — how work is delegated and handed back.

## Layout

```
projects/<name>/      one project: README or AGENTS.md, then whatever it needs
                      (code subpackages, notebooks/, notes/, tests/). Markdown-only is fine.
docs/                 workbench-wide reference only (KaTeX cheatsheet)
data/                 local data, not project-specific
scripts/              repo tooling
archive/              parked threads. Not maintained, not linted, not tested.
```

Code imports as `projects.<name>.<module>` — e.g. `from projects.stochastics.prob_models import
regime_chain`. There is no workspace and nothing to register. `make project NAME=<name>` scaffolds
a new one: a README and an `__init__.py`, nothing more. Add folders when the work asks for them.

Tests live in each project's `tests/` and are collected with `--import-mode=importlib`, so test
file names only need to be unique within a project.

## Rules

- `archive/` is read-only history. Don't refactor it, lint it, or fold it back in unrevised.
- Nothing crosses between projects implicitly. If one project imports another, say so in the
  importing project's README.

## Gate

```bash
make gate      # ruff check + ruff format --check + pytest across all projects
```

A project may add to this (the stochastics thread also requires its notebook to execute).

## Environment

```bash
uv sync                      # everything the live projects need
uv sync --group archive      # + torch and pysr, only for archive/toy_world_model
```

### Notebook kernel

Notebooks must run on the **`Python (workbench)`** kernel — this repo's `.venv`. It is pinned in
each notebook's metadata and registered with:

```bash
uv run python -m ipykernel install --user --name workbench --display-name "Python (workbench)"
```

If a cell reports `ModuleNotFoundError: No module named 'projects.<name>'`, check the kernel before
the install:

```python
import projects; print(projects.__path__)   # must be .../workbench/projects
```

History: the root package used to be `labs`, which collided with `~/repos/iris/labs` — a
different project whose `Python (labs)` kernel silently imported the wrong code. Keep root package
names specific to this repo.
