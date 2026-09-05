# workbench

A personal workbench for STEM exploration and small builds. Its current tenant is a
**stochastics learning thread**: working through the material of Ross, *Introduction to
Probability Models*, by building first and using the text as an examination layer rather than a
curriculum.

Start with [`docs/CHARTER.md`](docs/CHARTER.md) for the method and
[`STATE-OF-PLAY.md`](STATE-OF-PLAY.md) for where things stand.

## Quick start

```bash
uv sync                                        # one venv, from pyproject.toml
uv run python -m labs.prob_models.regime_chain # the founding example, with theory tripwires
make gate                                      # lint + format + tests
make notebook                                  # jupyter lab in notebooks/
```

## Layout

| Path | What's there |
|---|---|
| `src/labs/` | The machinery. Anything over ~30 lines lives here, not in a notebook. |
| `tests/` | Tripwires — hand-derived theory checked against the code. |
| `notebooks/` | The journey. Every claim runs. |
| `notes/` | `LORE.md` (the bug ledger), `patterns/`, `worked/` |
| `docs/` | Charter and reference |
| `archive/` | Parked threads — see [`archive/README.md`](archive/README.md) |

## Adding a lab

```bash
make lab NAME=arrival_streams
```

Creates `src/labs/arrival_streams/` and `tests/arrival_streams/`. Import it as
`from labs.arrival_streams import ...`; run it with
`uv run python -m labs.arrival_streams.main`. One package, one venv, one `pyproject.toml` —
nothing to register.
