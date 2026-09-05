#!/usr/bin/env bash
set -euo pipefail

# setup-web.sh
# Initialize the web workspace with pnpm and Vite

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "==> Setting up web workspace structure..."

# Create web workspace directories
mkdir -p "$REPO_ROOT/web/apps"
mkdir -p "$REPO_ROOT/web/packages"

cd "$REPO_ROOT/web"

echo "==> Checking for Node.js..."
if ! command -v node &> /dev/null; then
  echo "ERROR: Node.js is not installed."
  echo "Install from: https://nodejs.org/"
  exit 1
fi

echo "==> Checking for pnpm..."
if ! command -v pnpm &> /dev/null; then
  echo "ERROR: pnpm is not installed."
  echo "Install it with: npm install -g pnpm"
  exit 1
fi

echo "==> Creating workspace package.json..."
if [ ! -f "package.json" ]; then
  cat > package.json <<'EOF'
{
  "name": "workbench-web",
  "version": "0.1.0",
  "private": true,
  "description": "Workbench web workspace",
  "scripts": {
    "dev": "echo 'Select a specific app to run' && exit 1",
    "build": "echo 'Select a specific app to build' && exit 1",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "format": "prettier --write \"**/*.{ts,tsx,json,css,md}\""
  },
  "devDependencies": {
    "@typescript-eslint/eslint-plugin": "^7.0.0",
    "@typescript-eslint/parser": "^7.0.0",
    "eslint": "^8.56.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "prettier": "^3.2.5",
    "typescript": "^5.3.3"
  }
}
EOF
  echo "Created web/package.json"
else
  echo "web/package.json already exists"
fi

echo "==> Creating pnpm workspace configuration..."
if [ ! -f "pnpm-workspace.yaml" ]; then
  cat > pnpm-workspace.yaml <<'EOF'
packages:
  - 'apps/*'
  - 'packages/*'
EOF
  echo "Created web/pnpm-workspace.yaml"
else
  echo "web/pnpm-workspace.yaml already exists"
fi

echo "==> Creating TypeScript configuration..."
if [ ! -f "tsconfig.json" ]; then
  cat > tsconfig.json <<'EOF'
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  }
}
EOF
  echo "Created web/tsconfig.json"
else
  echo "web/tsconfig.json already exists"
fi

echo "==> Creating ESLint configuration..."
if [ ! -f ".eslintrc.cjs" ]; then
  cat > .eslintrc.cjs <<'EOF'
module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parser: '@typescript-eslint/parser',
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': [
      'warn',
      { allowConstantExport: true },
    ],
  },
}
EOF
  echo "Created web/.eslintrc.cjs"
else
  echo "web/.eslintrc.cjs already exists"
fi

echo "==> Creating Prettier configuration..."
if [ ! -f ".prettierrc.json" ]; then
  cat > .prettierrc.json <<'EOF'
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100
}
EOF
  echo "Created web/.prettierrc.json"
else
  echo "web/.prettierrc.json already exists"
fi

echo "==> Installing workspace dependencies..."
pnpm install

echo ""
echo "✅ Web workspace setup complete!"
echo ""
echo "Next steps:"
echo "  1. Create a new React app:"
echo "     ./scripts/new-web-app.sh my-app"
echo ""
echo "  2. Create a shared package (if needed):"
echo "     ./scripts/new-web-package.sh my-components"
echo ""
