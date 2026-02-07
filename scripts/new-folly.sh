#!/usr/bin/env bash
set -euo pipefail

# new-folly.sh <name>
# Create a new experimental Python project in follies/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <name>"
  echo "Example: $0 my-experiment"
  exit 1
fi

PROJECT_NAME="$1"
PROJECT_DIR="$REPO_ROOT/py/packages/follies/$PROJECT_NAME"
PACKAGE_NAME="${PROJECT_NAME//-/_}"

if [ -d "$PROJECT_DIR" ]; then
  echo "ERROR: Project '$PROJECT_NAME' already exists at $PROJECT_DIR"
  exit 1
fi

echo "==> Creating folly: $PROJECT_NAME"

# Create directory structure
mkdir -p "$PROJECT_DIR/src/$PACKAGE_NAME"
mkdir -p "$PROJECT_DIR/tests"

# Create pyproject.toml
cat > "$PROJECT_DIR/pyproject.toml" <<EOF
[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "Experimental project: $PROJECT_NAME"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
EOF

# Create main.py
cat > "$PROJECT_DIR/src/$PACKAGE_NAME/main.py" <<EOF
"""
$PROJECT_NAME

Quick experiment - not meant to be polished.
"""


def main():
    print("Hello from $PROJECT_NAME!")


if __name__ == "__main__":
    main()
EOF

# Create __init__.py
cat > "$PROJECT_DIR/src/$PACKAGE_NAME/__init__.py" <<EOF
"""$PROJECT_NAME"""

__version__ = "0.1.0"
EOF

# Create smoke test
cat > "$PROJECT_DIR/tests/test_smoke.py" <<EOF
"""Smoke test for $PROJECT_NAME"""

from ${PACKAGE_NAME} import main


def test_main_runs():
    """Verify main() executes without error"""
    main.main()
EOF

# Create README
cat > "$PROJECT_DIR/README.md" <<EOF
# $PROJECT_NAME

**Intent**: Folly (experimental)

## What

Quick description of what you're exploring.

## Why

Why you're building this / what you want to learn.

## Run

\`\`\`bash
# From py/ directory with venv activated
python -m ${PACKAGE_NAME}.main
\`\`\`

## Test

\`\`\`bash
pytest packages/follies/$PROJECT_NAME
\`\`\`
EOF

echo "✅ Created folly: $PROJECT_NAME"
echo ""
echo "Location: $PROJECT_DIR"
echo ""
echo "Next steps:"
echo "  cd py"
echo "  source .venv/bin/activate  # if not already activated"
echo "  python -m ${PACKAGE_NAME}.main"
echo "  pytest packages/follies/$PROJECT_NAME"
echo ""
