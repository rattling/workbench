#!/usr/bin/env bash
set -euo pipefail

# new-project.sh <name>
#
# Creates projects/<name>/ with a README and an empty package stub, nothing else.
# Add notes/, notebooks/, tests/ or code subpackages when the work asks for them.
#   import as:  from projects.<name>.<module> import ...

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ $# -ne 1 ]; then
  echo "Usage: $0 <name>    e.g. $0 bioplastics"
  exit 1
fi

MODULE="${1//-/_}"
DIR="$ROOT/projects/$MODULE"

if [ -d "$DIR" ]; then
  echo "ERROR: projects/$MODULE already exists"
  exit 1
fi

mkdir -p "$DIR"
echo "\"\"\"$MODULE\"\"\"" > "$DIR/__init__.py"
cat > "$DIR/README.md" <<README
# $MODULE

*What this project is for, in a sentence or two.*
README

echo "✅ projects/$MODULE"
echo "   import: from projects.$MODULE.<module> import ..."
