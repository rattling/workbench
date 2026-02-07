#!/usr/bin/env bash
set -euo pipefail

# new-web-app.sh <name>
# Create a new React + Vite app in web/apps/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <name>"
  echo "Example: $0 my-app"
  exit 1
fi

PROJECT_NAME="$1"
PROJECT_DIR="$REPO_ROOT/web/apps/$PROJECT_NAME"

if [ -d "$PROJECT_DIR" ]; then
  echo "ERROR: Project '$PROJECT_NAME' already exists at $PROJECT_DIR"
  exit 1
fi

echo "==> Creating web app: $PROJECT_NAME"

# Create directory structure
mkdir -p "$PROJECT_DIR/src"
mkdir -p "$PROJECT_DIR/public"

# Create package.json
cat > "$PROJECT_DIR/package.json" <<EOF
{
  "name": "$PROJECT_NAME",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext ts,tsx",
    "format": "prettier --write \"src/**/*.{ts,tsx,css}\""
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.55",
    "@types/react-dom": "^18.2.19",
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.1.0"
  }
}
EOF

# Create tsconfig.json
cat > "$PROJECT_DIR/tsconfig.json" <<'EOF'
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
EOF

# Create tsconfig.node.json
cat > "$PROJECT_DIR/tsconfig.node.json" <<'EOF'
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
EOF

# Create vite.config.ts
cat > "$PROJECT_DIR/vite.config.ts" <<'EOF'
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
  },
});
EOF

# Create index.html
cat > "$PROJECT_DIR/index.html" <<EOF
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>$PROJECT_NAME</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
EOF

# Create main.tsx
cat > "$PROJECT_DIR/src/main.tsx" <<'EOF'
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
EOF

# Create App.tsx
cat > "$PROJECT_DIR/src/App.tsx" <<EOF
import { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="app">
      <h1>$PROJECT_NAME</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
      <p className="hint">
        Edit <code>src/App.tsx</code> and save to test HMR
      </p>
    </div>
  );
}

export default App;
EOF

# Create index.css
cat > "$PROJECT_DIR/src/index.css" <<'EOF'
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
}
EOF

# Create App.css
cat > "$PROJECT_DIR/src/App.css" <<'EOF'
.app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

.card {
  padding: 2em;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}

button:hover {
  border-color: #646cff;
}

button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

.hint {
  color: #888;
}

@media (prefers-color-scheme: light) {
  button {
    background-color: #f9f9f9;
  }
}
EOF

# Create README
cat > "$PROJECT_DIR/README.md" <<EOF
# $PROJECT_NAME

React + TypeScript + Vite app

## Development

\`\`\`bash
# From web/apps/$PROJECT_NAME
pnpm install
pnpm dev
\`\`\`

## Build

\`\`\`bash
pnpm build
pnpm preview
\`\`\`

## Lint & Format

\`\`\`bash
pnpm lint
pnpm format
\`\`\`
EOF

# Create .gitignore
cat > "$PROJECT_DIR/.gitignore" <<'EOF'
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
EOF

cd "$REPO_ROOT/web"
echo "==> Installing dependencies for $PROJECT_NAME..."
pnpm install

echo ""
echo "✅ Created web app: $PROJECT_NAME"
echo ""
echo "Location: $PROJECT_DIR"
echo ""
echo "Next steps:"
echo "  cd web/apps/$PROJECT_NAME"
echo "  pnpm dev"
echo ""
