#!/usr/bin/env bash
set -euo pipefail

# setup-repo.sh
# Initialize the workbench repository structure and Python environment

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "==> Setting up workbench repository structure..."

# Create top-level directories
mkdir -p "$REPO_ROOT/notes"
mkdir -p "$REPO_ROOT/data"
mkdir -p "$REPO_ROOT/tools"

# Create Python workspace structure
mkdir -p "$REPO_ROOT/py/packages/apps"
mkdir -p "$REPO_ROOT/py/packages/follies"
mkdir -p "$REPO_ROOT/py/packages/rube"
mkdir -p "$REPO_ROOT/py/packages/lib"

# Create web workspace structure (commented out - can enable when needed)
# mkdir -p "$REPO_ROOT/web/apps"
# mkdir -p "$REPO_ROOT/web/packages"

echo "==> Creating .gitignore if it doesn't exist..."
if [ ! -f "$REPO_ROOT/.gitignore" ]; then
  cat > "$REPO_ROOT/.gitignore" <<'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
env/
*.egg-info/
dist/
build/
.pytest_cache/
.ruff_cache/
.mypy_cache/
.pytype/

# Data
data/*
!data/.gitkeep

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Env files
.env
.env.local

# Node (future)
node_modules/
.pnpm-store/
EOF
  echo "Created .gitignore"
else
  echo ".gitignore already exists"
fi

echo "==> Creating .env.example if it doesn't exist..."
if [ ! -f "$REPO_ROOT/.env.example" ]; then
  cat > "$REPO_ROOT/.env.example" <<'EOF'
# Environment variables for workbench
# Copy to .env and fill in actual values

# Add your environment variables here as needed
# EXAMPLE_API_KEY=your_key_here
EOF
  echo "Created .env.example"
else
  echo ".env.example already exists"
fi

# Create .gitkeep for data directory
touch "$REPO_ROOT/data/.gitkeep"

echo "==> Checking for uv..."
if ! command -v uv &> /dev/null; then
  echo "ERROR: uv is not installed."
  echo "Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 1
fi

echo "==> Setting up Python workspace with uv..."
cd "$REPO_ROOT/py"

# Create pyproject.toml for workspace root
if [ ! -f "pyproject.toml" ]; then
  cat > pyproject.toml <<'EOF'
[project]
name = "workbench"
version = "0.1.0"
description = "Workbench Python workspace"
requires-python = ">=3.11"

[tool.uv.workspace]
members = ["packages/*/*"]

[tool.uv.sources]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]
ignore = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.pytest.ini_options]
testpaths = ["packages"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
EOF
  echo "Created py/pyproject.toml"
else
  echo "py/pyproject.toml already exists"
fi

echo "==> Creating Python 3.11 virtual environment with uv..."
uv venv --python 3.11

echo "==> Installing base development tools..."
uv pip install ruff pytest

echo ""
echo "✅ Repository setup complete!"
echo ""
echo "Next steps:"
echo "  1. Activate the Python environment:"
echo "     source py/.venv/bin/activate"
echo ""
echo "  2. Create a new project:"
echo "     ./scripts/new-folly.sh my-experiment"
echo "     ./scripts/new-app.sh my-app"
echo "     ./scripts/new-rube.sh my-overengineered-thing"
echo ""
