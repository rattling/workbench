.PHONY: help new-lab powell-run powell-compare powell-all clean-runs

# Default parameters (can override: make powell-all T=56)
T ?= 28
SEED ?= 42

help:
	@echo "Available targets:"
	@echo "  new-lab         - Create a new lab package (NAME=<name>)"
	@echo "  powell-all      - Run both policies and compare results"
	@echo "  powell-run      - Run both Policy A and Policy B"
	@echo "  powell-compare  - Compare existing trace files"
	@echo "  clean-runs      - Remove generated trace files"
	@echo ""
	@echo "Parameters:"
	@echo "  NAME=<name>     - Lab name for new-lab"
	@echo "  T=<num>         - Number of time periods (default: 28)"
	@echo "  SEED=<num>      - Random seed (default: 42)"
	@echo ""
	@echo "Examples:"
	@echo "  make new-lab NAME=p2-optimisation"
	@echo "  make powell-all T=56 SEED=99"

new-lab:
	@test -n "$(NAME)" || (echo "Usage: make new-lab NAME=<name>  (add FULL=1 for standalone package)"; exit 1)
	@if [ "$(FULL)" = "1" ]; then \
	  cd .. && bash scripts/new-lab.sh --full $(NAME); \
	else \
	  cd .. && bash scripts/new-lab.sh $(NAME); \
	fi

powell-run:
	@echo "==> Running Policy A (T=$(T), seed=$(SEED))..."
	@python -m powell_sdm_lab.main --policy a --seed $(SEED) --T $(T)
	@echo ""
	@echo "==> Running Policy B (T=$(T), seed=$(SEED))..."
	@python -m powell_sdm_lab.main --policy b --seed $(SEED) --T $(T)

powell-compare:
	@echo ""
	@python -m powell_sdm_lab.compare

powell-all: powell-run powell-compare
	@echo ""
	@echo "✅ Complete! Trace files available in packages/labs/runs/"

clean-runs:
	@rm -f packages/labs/runs/policy_*.txt
	@echo "Cleaned run outputs"
