#!/usr/bin/env bash
set -euo pipefail

# new-lab.sh <name>
#
# Creates a lab under src/labs/<name>/ with a matching tests/<name>/.
#   import as:  from labs.<name> import ...
#   run as:     uv run python -m labs.<name>.main
#   test as:    uv run pytest tests/<name>
#
# One package, one venv, one pyproject. Nothing to register.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ $# -ne 1 ]; then
  echo "Usage: $0 <name>    e.g. $0 arrival_streams"
  exit 1
fi

MODULE="${1//-/_}"
LAB="$ROOT/src/labs/$MODULE"
TESTS="$ROOT/tests/$MODULE"

if [ -d "$LAB" ]; then
  echo "ERROR: labs.$MODULE already exists at $LAB"
  exit 1
fi

mkdir -p "$LAB" "$TESTS"

cat > "$LAB/__init__.py" <<EOF
"""$MODULE"""
EOF

cat > "$LAB/main.py" <<EOF
"""$MODULE — predictions on paper first, then run this."""


def main():
    print("Hello from labs.$MODULE!")


if __name__ == "__main__":
    main()
EOF

cat > "$TESTS/test_${MODULE}.py" <<EOF
"""Tripwires for $MODULE — assert against theory derived by hand, not against
the code's own arithmetic."""

from labs.$MODULE import main


def test_main_runs():
    main.main()
EOF

echo "✅ src/labs/$MODULE  +  tests/$MODULE"
echo "   run:  uv run python -m labs.$MODULE.main"
echo "   test: uv run pytest tests/$MODULE"
