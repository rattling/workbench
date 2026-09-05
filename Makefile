.PHONY: help setup lab test lint fmt gate notebook

help:
	@echo "  make setup            - create/refresh the venv from pyproject.toml"
	@echo "  make lab NAME=<name>  - scaffold src/labs/<name> + tests/<name>"
	@echo "  make gate             - lint + format check + tests (the acceptance gate)"
	@echo "  make test             - pytest only"
	@echo "  make lint / fmt       - ruff check / ruff format"
	@echo "  make notebook         - launch jupyter lab"
	@echo ""
	@echo "  archived labs need their heavy deps:  uv sync --group archive"

setup:
	uv sync

lab:
	@test -n "$(NAME)" || (echo "Usage: make lab NAME=<name>"; exit 1)
	@bash scripts/new-lab.sh $(NAME)

test:
	uv run pytest -q

lint:
	uv run ruff check .

fmt:
	uv run ruff format .

gate:
	uv run ruff check .
	uv run ruff format --check .
	uv run pytest -q

notebook:
	uv run --with jupyterlab jupyter lab notebooks/
