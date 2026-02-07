# workbench

Prototypes for everything. A single repository for high-velocity STEM exploration, learning, and small builds.

## Quick Start

### First Time Setup

```bash
# Initialize repository structure and Python environment
./scripts/setup-repo.sh

# Activate Python environment
source py/.venv/bin/activate
```

### Create a New Project

```bash
# Quick experiment (minimal structure)
./scripts/new-folly.sh my-experiment

# Use-case driven app (more structure)
./scripts/new-app.sh my-app

# Deliberately overengineered (full ceremony)
./scripts/new-rube.sh my-complex-thing
```

### Daily Workflow

```bash
# Activate environment
source py/.venv/bin/activate

# Run a project
cd py
python -m my_project.main

# Test a project
pytest packages/follies/my-experiment

# Format and lint
ruff format packages/apps/my-app
ruff check packages/apps/my-app
```

## Philosophy

Read [REPO_SETUP.md](REPO_SETUP.md) for the full design philosophy and structure.

**TL;DR**: Start here by default. Build fast. Graduate projects to their own repos only when this becomes a genuine constraint.
