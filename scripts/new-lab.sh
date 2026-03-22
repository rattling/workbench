#!/usr/bin/env bash
set -euo pipefail

# new-lab.sh <name>
#
# Create a new lab package under packages/labs/.
# The Python module name is derived by replacing hyphens with underscores.
#
# Examples:
#   ./new-lab.sh phase1-randomness-uncertainty
#   ./new-lab.sh markov-chains

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <name>"
  echo ""
  echo "Examples:"
  echo "  $0 phase1-randomness-uncertainty"
  echo "  $0 markov-chains"
  exit 1
fi

NAME="$1"
PKG_DIR="$REPO_ROOT/py/packages/labs/$NAME"
MODULE="${NAME//-/_}"

if [ -d "$PKG_DIR" ]; then
  echo "ERROR: '$NAME' already exists at $PKG_DIR"
  exit 1
fi

echo "==> Creating lab: $NAME (module: $MODULE)"

mkdir -p "$PKG_DIR/src/$MODULE"
mkdir -p "$PKG_DIR/tests"

cat > "$PKG_DIR/pyproject.toml" <<EOF
[project]
name = "$NAME"
version = "0.1.0"
description = "$NAME"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
EOF

cat > "$PKG_DIR/src/$MODULE/__init__.py" <<EOF
"""$NAME"""
EOF

cat > "$PKG_DIR/src/$MODULE/main.py" <<EOF
"""$NAME"""


def main():
    print("Hello from $NAME!")


if __name__ == "__main__":
    main()
EOF

cat > "$PKG_DIR/tests/test_smoke.py" <<EOF
"""Smoke test for $NAME"""

from $MODULE import main


def test_main_runs():
    main.main()
EOF

cat > "$PKG_DIR/README.md" <<EOF
# $NAME

## Run

\`\`\`bash
# From py/ directory
python -m ${MODULE}.main
\`\`\`

## Test

\`\`\`bash
pytest packages/labs/$NAME
\`\`\`
EOF

echo ""
echo "✅ $PKG_DIR"
echo ""

cd "$REPO_ROOT/py"
uv sync

echo ""
echo "  python -m ${MODULE}.main"
echo "  pytest packages/labs/$NAME"
echo ""

