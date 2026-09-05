#!/usr/bin/env bash
set -euo pipefail

# new-rube.sh <name>
# Create a new deliberately overengineered Python project in rube/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <name>"
  echo "Example: $0 my-overengineered-thing"
  exit 1
fi

PROJECT_NAME="$1"
PROJECT_DIR="$REPO_ROOT/py/packages/rube/$PROJECT_NAME"
PACKAGE_NAME="${PROJECT_NAME//-/_}"

if [ -d "$PROJECT_DIR" ]; then
  echo "ERROR: Project '$PROJECT_NAME' already exists at $PROJECT_DIR"
  exit 1
fi

echo "==> Creating rube: $PROJECT_NAME"

# Create directory structure with more ceremony
mkdir -p "$PROJECT_DIR/src/$PACKAGE_NAME"
mkdir -p "$PROJECT_DIR/tests/unit"
mkdir -p "$PROJECT_DIR/tests/integration"

# Create pyproject.toml
cat > "$PROJECT_DIR/pyproject.toml" <<EOF
[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "Rube Goldberg project: $PROJECT_NAME"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP", "ANN", "S", "B"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "--cov=src/${PACKAGE_NAME} --cov-report=term-missing"
EOF

# Create main.py
cat > "$PROJECT_DIR/src/$PACKAGE_NAME/main.py" <<EOF
"""
$PROJECT_NAME

Deliberately overengineered for learning and exploration.
"""


def main() -> None:
    """Application entry point with proper ceremony"""
    print("Welcome to $PROJECT_NAME - where simple things become complex!")
    print("This is where abstractions, patterns, and infra come to play.")


if __name__ == "__main__":
    main()
EOF

# Create __init__.py
cat > "$PROJECT_DIR/src/$PACKAGE_NAME/__init__.py" <<EOF
"""
$PROJECT_NAME

A Rube Goldberg machine for learning.
"""

__version__ = "0.1.0"
EOF

# Create unit test
cat > "$PROJECT_DIR/tests/unit/test_main.py" <<EOF
"""Unit tests for $PROJECT_NAME main module"""

from ${PACKAGE_NAME} import main


def test_main_runs():
    """Verify main() executes without error"""
    main.main()
EOF

# Create integration test placeholder
cat > "$PROJECT_DIR/tests/integration/test_end_to_end.py" <<EOF
"""Integration tests for $PROJECT_NAME"""

import pytest


@pytest.mark.skip(reason="Add integration tests as complexity grows")
def test_placeholder():
    """Placeholder for future integration tests"""
    pass
EOF

# Create README
cat > "$PROJECT_DIR/README.md" <<EOF
# $PROJECT_NAME

**Intent**: Rube (deliberate overengineering for learning)

## Purpose

Describe the deliberately complex thing you're building to understand systems, patterns, or infrastructure.

## Philosophy

This is where we:
- Try frameworks and orchestration
- Build abstractions for their own sake
- Explore infra patterns
- Learn by overbuilding

**This is not meant to be practical.** It's meant to be educational.

## Usage

\`\`\`bash
# From py/ directory with venv activated
python -m ${PACKAGE_NAME}.main
\`\`\`

## Development

### Install with dev dependencies

\`\`\`bash
uv pip install -e packages/rube/$PROJECT_NAME[dev]
\`\`\`

### Run tests with coverage

\`\`\`bash
pytest packages/rube/$PROJECT_NAME
\`\`\`

### Format and lint

\`\`\`bash
ruff format packages/rube/$PROJECT_NAME
ruff check packages/rube/$PROJECT_NAME
\`\`\`

## Architecture

Document your glorious over-architecture here:

- **src/${PACKAGE_NAME}/**: Core package
- **tests/unit/**: Unit tests
- **tests/integration/**: Integration tests

Add more layers as you go overboard! 🎨
EOF

echo "✅ Created rube: $PROJECT_NAME"
echo ""
echo "Location: $PROJECT_DIR"
echo ""
echo "Next steps:"
echo "  cd py"
echo "  source .venv/bin/activate  # if not already activated"
echo "  uv pip install -e packages/rube/$PROJECT_NAME[dev]"
echo "  python -m ${PACKAGE_NAME}.main"
echo "  pytest packages/rube/$PROJECT_NAME"
echo ""
echo "Now go forth and overengineer! 🎭"
echo ""
