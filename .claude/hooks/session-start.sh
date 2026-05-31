#!/bin/bash
set -euo pipefail

# Only run in remote Claude Code on the web sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

echo '{"async": true, "asyncTimeout": 300000}'

# Install uipro-cli globally if not present
if ! command -v uipro &>/dev/null; then
  npm install -g uipro-cli
fi

# Register playwright-skill MCP server if not already configured
if ! claude mcp list 2>/dev/null | grep -q "playwright-skill"; then
  claude mcp add playwright-skill -- npx --yes @anthropic-ai/claude-code-mcp-server skill \
    https://github.com/lackeyjb/playwright-skill/releases/download/v4.1.0/playwright-skill.tar.gz
fi

# Install graphifyy Python CLI if not present
if ! command -v graphify &>/dev/null; then
  pip install graphifyy
fi

# Reinstall impeccable plugin if settings exist but plugin not active
if [ -f "$CLAUDE_PROJECT_DIR/.claude/settings.json" ]; then
  if grep -q "impeccable" "$CLAUDE_PROJECT_DIR/.claude/settings.json" 2>/dev/null; then
    if ! claude plugin list 2>/dev/null | grep -q "impeccable"; then
      npx claudepluginhub pbakaus/impeccable --plugin impeccable 2>/dev/null || true
    fi
  fi
fi
