#!/usr/bin/env bash
set -euo pipefail

# new-lab.sh [-f] <name>
#
# Default: create a simple subpackage under the shared labs package.
#   - lives in packages/labs/src/labs/<name>/
#   - shares the workspace .venv and uv
#   - import as: from labs.<name> import ...
#   - run as:    uv run python -m labs.<name>.main
#
# -f / --full: create a standalone workspace package with its own pyproject.toml
#   under packages/labs/<name>/  (useful for larger, more isolated work)
#
# Examples:
#   ./new-lab.sh markov-chains
#   ./new-lab.sh -f big-project

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LABS_PKG="$REPO_ROOT/py/packages/labs"

FULL=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    -f|--full) FULL=1; shift ;;
    -*) echo "Unknown option: $1"; exit 1 ;;
    *) break ;;
  esac
done

if [ $# -lt 1 ]; then
  echo "Usage: $0 [-f] <name>"
  echo ""
  echo "  Default: simple subpackage in shared labs package"
  echo "  -f/--full: standalone package with own pyproject.toml"
  echo ""
  echo "Examples:"
  echo "  $0 markov-chains"
  echo "  $0 -f big-project"
  exit 1
fi

NAME="$1"
MODULE="${NAME//-/_}"

if [ "$FULL" -eq 1 ]; then
  # --- Standalone package ---
  PKG_DIR="$LABS_PKG/$NAME"

  if [ -d "$PKG_DIR" ]; then
    echo "ERROR: '$NAME' already exists at $PKG_DIR"
    exit 1
  fi

  echo "==> Creating standalone lab: $NAME (module: $MODULE)"

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

  echo ""
  echo "✅ $PKG_DIR"
  echo "   Run:  cd py && uv run python -m ${MODULE}.main"
  echo ""

else
  # --- Simple subpackage in shared labs package ---
  MODULE_DIR="$LABS_PKG/src/labs/$MODULE"
  TEST_DIR="$LABS_PKG/tests/$MODULE"

  if [ -d "$MODULE_DIR" ]; then
    echo "ERROR: labs.$MODULE already exists at $MODULE_DIR"
    exit 1
  fi

  echo "==> Creating lab: labs.$MODULE"

  mkdir -p "$MODULE_DIR"
  mkdir -p "$TEST_DIR"

  cat > "$MODULE_DIR/__init__.py" <<EOF
"""$NAME"""
EOF

  cat > "$MODULE_DIR/main.py" <<EOF
"""$NAME"""


def main():
    print("Hello from $NAME!")


if __name__ == "__main__":
    main()
EOF

  cat > "$TEST_DIR/test_smoke.py" <<EOF
"""Smoke test for $NAME"""

from labs.$MODULE import main


def test_main_runs():
    main.main()
EOF

  echo ""
  echo "✅ $MODULE_DIR"
  echo "   Import: from labs.$MODULE import ..."
  echo "   Run:    cd py && uv run python -m labs.${MODULE}.main"
  echo ""
fi

cd "$REPO_ROOT/py"
uv sync

echo ""
echo "  python -m ${MODULE}.main"
echo "  pytest packages/labs/$NAME"
echo ""

