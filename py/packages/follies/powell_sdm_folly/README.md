# Powell SDM Folly — Trace‑First Exploration

**Intent**: Folly (experimental, pedagogical)

## What

A minimal implementation of Powell's Sequential Decision-Making loop for inventory control.

This project exists to build intuition for the SDM framework by making the full loop visible:

```
S_t → x_t → S^x_t → W_{t+1} → S_{t+1} → learning → repeat
```

Two policies run on the same demand sequence:
- **Policy A**: Constant base-stock (no learning)
- **Policy B**: Forecast-driven base-stock with online demand model

The primary output is **human-readable trace files** showing step-by-step decisions and outcomes.

## Run

```bash
# From py/ directory with venv activated

# Install the package (first time only)
uv pip install -e packages/follies/powell_sdm_folly

# Run Policy A (constant base-stock)
python -m powell_sdm_folly.main --policy a --seed 42 --T 28

# Run Policy B (forecast-driven with learning)
python -m powell_sdm_folly.main --policy b --seed 42 --T 28

# Compare both policies
python -m powell_sdm_folly.compare
```

## Output

Trace files are written to `runs/`:
- `policy_a_latest.txt` — Policy A trace
- `policy_b_latest.txt` — Policy B trace

Each line shows:
- State, decision, post-decision state
- Exogenous information (demand)
- Transition (sales, next state)
- Costs and stockouts
- Forecasts and errors (Policy B only)

## Test

```bash
pytest packages/follies/powell_sdm_folly
```

## Why

To see Powell's framework operating explicitly and understand how learning integrates into the decision loop.

Not meant to be performant or reusable—just pedagogical.
