#!/usr/bin/env bash
set -euo pipefail

# new-app.sh <name>
# Create a new use-case driven Python project in apps/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <name>"
  echo "Example: $0 my-app"
  exit 1
fi

PROJECT_NAME="$1"
PROJECT_DIR="$REPO_ROOT/py/packages/apps/$PROJECT_NAME"
PACKAGE_NAME="${PROJECT_NAME//-/_}"

if [ -d "$PROJECT_DIR" ]; then
  echo "ERROR: Project '$PROJECT_NAME' already exists at $PROJECT_DIR"
  exit 1
fi

echo "==> Creating app: $PROJECT_NAME"

# Create directory structure
mkdir -p "$PROJECT_DIR/src/$PACKAGE_NAME"
mkdir -p "$PROJECT_DIR/tests"

# Create pyproject.toml
cat > "$PROJECT_DIR/pyproject.toml" <<EOF
[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "Application: $PROJECT_NAME"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]
EOF

# Create main.py
cat > "$PROJECT_DIR/src/$PACKAGE_NAME/main.py" <<EOF
"""
$PROJECT_NAME

Main application entry point.
"""


def main():
    """Application entry point"""
    print("Running $PROJECT_NAME")


if __name__ == "__main__":
    main()
EOF

# Create __init__.py
cat > "$PROJECT_DIR/src/$PACKAGE_NAME/__init__.py" <<EOF
"""$PROJECT_NAME"""

__version__ = "0.1.0"
EOF

# Create comprehensive test
cat > "$PROJECT_DIR/tests/test_main.py" <<EOF
"""Tests for $PROJECT_NAME"""

import pytest
from ${PACKAGE_NAME} import main


def test_main_runs():
    """Verify main() executes without error"""
    main.main()


# Add more tests as the app grows
EOF

# Create README
cat > "$PROJECT_DIR/README.md" <<EOF
# $PROJECT_NAME

**Intent**: App (use-case driven, maintainable)

## Purpose

Clear description of what this app does and why it exists.

## Usage

\`\`\`bash
# From py/ directory with venv activated
python -m ${PACKAGE_NAME}.main
\`\`\`

## Development

### Run tests

\`\`\`bash
pytest packages/apps/$PROJECT_NAME
\`\`\`

### Format code

\`\`\`bash
ruff format packages/apps/$PROJECT_NAME
\`\`\`

### Lint

\`\`\`bash
ruff check packages/apps/$PROJECT_NAME
\`\`\`

## Dependencies

Dependencies are managed in \`pyproject.toml\`. Install with:

\`\`\`bash
uv pip install -e packages/apps/$PROJECT_NAME[dev]
\`\`\`

## Architecture

Add notes here as structure emerges:

- **main.py**: Entry point
- *Add more as needed - avoid empty layers*
EOF

echo "✅ Created app: $PROJECT_NAME"
echo ""
echo "Location: $PROJECT_DIR"
echo ""
echo "Next steps:"
echo "  cd py"
echo "  source .venv/bin/activate  # if not already activated"
echo "  uv pip install -e packages/apps/$PROJECT_NAME[dev]"
echo "  python -m ${PACKAGE_NAME}.main"
echo "  pytest packages/apps/$PROJECT_NAME"
echo ""
