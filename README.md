# workbench

A personal workbench for STEM exploration and small builds, organised as self-contained projects
that share one package and one venv.

| Project | What it is |
|---|---|
| [`projects/stochastics/`](projects/stochastics/) | Ross, *Introduction to Probability Models*, build-first — see its [charter](projects/stochastics/CHARTER.md) and [state of play](projects/stochastics/STATE-OF-PLAY.md) |
| [`projects/bioplastics/`](projects/bioplastics/) | Researching and modelling biodegradable plastics |

## Quick start

```bash
uv sync                                                  # one venv, from pyproject.toml
uv run python -m projects.stochastics.prob_models.regime_chain
make gate                                                # lint + format + tests, all projects
make notebook                                            # jupyter lab at projects/
make project NAME=<name>                                 # start a new project
```

## Layout

| Path | What's there |
|---|---|
| `projects/<name>/` | One project: its code, notebooks, notes and tests together. Imports as `projects.<name>.…` |
| `docs/` | Workbench-wide reference |
| `archive/` | Parked threads — see [`archive/README.md`](archive/README.md) |

See [`AGENTS.md`](AGENTS.md) for conventions.
