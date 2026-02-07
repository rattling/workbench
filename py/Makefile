.PHONY: help powell-run powell-compare powell-all clean-runs

# Default parameters (can override: make powell-all T=56)
T ?= 28
SEED ?= 42

help:
	@echo "Available targets:"
	@echo "  powell-all      - Run both policies and compare results"
	@echo "  powell-run      - Run both Policy A and Policy B"
	@echo "  powell-compare  - Compare existing trace files"
	@echo "  clean-runs      - Remove generated trace files"
	@echo ""
	@echo "Parameters:"
	@echo "  T=<num>         - Number of time periods (default: 28)"
	@echo "  SEED=<num>      - Random seed (default: 42)"
	@echo ""
	@echo "Example: make powell-all T=56 SEED=99"

powell-run:
	@echo "==> Running Policy A (T=$(T), seed=$(SEED))..."
	@python -m powell_sdm_folly.main --policy a --seed $(SEED) --T $(T)
	@echo ""
	@echo "==> Running Policy B (T=$(T), seed=$(SEED))..."
	@python -m powell_sdm_folly.main --policy b --seed $(SEED) --T $(T)

powell-compare:
	@echo ""
	@python -m powell_sdm_folly.compare

powell-all: powell-run powell-compare
	@echo ""
	@echo "✅ Complete! Trace files available in packages/follies/runs/"

clean-runs:
	@rm -f packages/follies/runs/policy_*.txt
	@echo "Cleaned run outputs"
