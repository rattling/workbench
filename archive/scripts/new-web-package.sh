#!/usr/bin/env bash
set -euo pipefail

# new-web-package.sh <name>
# Create a new shared package in web/packages/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <name>"
  echo "Example: $0 ui-components"
  exit 1
fi

PROJECT_NAME="$1"
PROJECT_DIR="$REPO_ROOT/web/packages/$PROJECT_NAME"

if [ -d "$PROJECT_DIR" ]; then
  echo "ERROR: Package '$PROJECT_NAME' already exists at $PROJECT_DIR"
  exit 1
fi

echo "==> Creating web package: $PROJECT_NAME"

# Create directory structure
mkdir -p "$PROJECT_DIR/src"

# Create package.json
cat > "$PROJECT_DIR/package.json" <<EOF
{
  "name": "@workbench/$PROJECT_NAME",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "main": "./src/index.ts",
  "types": "./src/index.ts",
  "exports": {
    ".": "./src/index.ts"
  },
  "scripts": {
    "lint": "eslint . --ext ts,tsx",
    "format": "prettier --write \"src/**/*.{ts,tsx}\""
  },
  "peerDependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.55",
    "@types/react-dom": "^18.2.19",
    "typescript": "^5.3.3"
  }
}
EOF

# Create tsconfig.json
cat > "$PROJECT_DIR/tsconfig.json" <<'EOF'
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "baseUrl": ".",
    "declaration": true,
    "declarationMap": true
  },
  "include": ["src"]
}
EOF

# Create index.ts
cat > "$PROJECT_DIR/src/index.ts" <<EOF
/**
 * $PROJECT_NAME
 * 
 * Shared components/utilities for workbench web apps
 */

export const version = '0.1.0';

// Export your components/utilities here
// export { Button } from './Button';
EOF

# Create example component
cat > "$PROJECT_DIR/src/example.tsx" <<'EOF'
/**
 * Example component
 * Delete or replace this with your actual components
 */

interface ExampleProps {
  text: string;
}

export function Example({ text }: ExampleProps) {
  return <div>{text}</div>;
}
EOF

# Create README
cat > "$PROJECT_DIR/README.md" <<EOF
# @workbench/$PROJECT_NAME

Shared package for workbench web apps

## Usage

In an app's package.json:

\`\`\`json
{
  "dependencies": {
    "@workbench/$PROJECT_NAME": "workspace:*"
  }
}
\`\`\`

Then import:

\`\`\`typescript
import { Example } from '@workbench/$PROJECT_NAME';
\`\`\`

## Development

This package is developed in the context of the workspace. Make changes here and they'll be reflected in apps that use it.
EOF

cd "$REPO_ROOT/web"
echo "==> Installing dependencies for $PROJECT_NAME..."
pnpm install

echo ""
echo "✅ Created web package: $PROJECT_NAME"
echo ""
echo "Location: $PROJECT_DIR"
echo ""
echo "To use in an app:"
echo "  1. Add to app's package.json dependencies:"
echo "     \"@workbench/$PROJECT_NAME\": \"workspace:*\""
echo "  2. Run 'pnpm install' in web/"
echo "  3. Import in your app code"
echo ""
