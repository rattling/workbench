.PHONY: help setup project test lint fmt gate notebook

help:
	@echo "  make setup                 - create/refresh the venv from pyproject.toml"
	@echo "  make project NAME=<name>   - scaffold projects/<name>/ (README + package stub)"
	@echo "  make gate                  - lint + format check + tests (the acceptance gate)"
	@echo "  make test                  - pytest only"
	@echo "  make lint / fmt            - ruff check / ruff format"
	@echo "  make notebook              - launch jupyter lab at projects/"
	@echo ""
	@echo "  archived labs need their heavy deps:  uv sync --group archive"

setup:
	uv sync

project:
	@test -n "$(NAME)" || (echo "Usage: make project NAME=<name>"; exit 1)
	@bash scripts/new-project.sh $(NAME)

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
	uv run --with jupyterlab jupyter lab projects/
