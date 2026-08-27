#!/usr/bin/env bash
# founder-playbook one-line installer — OpenCode + Claude Code
# Usage: curl -fsSL https://raw.githubusercontent.com/xeonmobius/founder-playbook/main/install.sh | bash
#    or: bash install.sh [--force]
set -euo pipefail
REPO="https://github.com/xeonmobius/founder-playbook.git"
FORCE="${1:-}"

install_to() {
  local dest="$1"
  local label="$2"
  if [ -d "$dest/.git" ]; then
    if [ "$FORCE" = "--force" ]; then
      echo "→ $label exists, --force: removing $dest"
      rm -rf "$dest"
    else
      echo "→ $label exists, updating $dest"
      git -C "$dest" pull --ff-only 2>/dev/null || git -C "$dest" fetch origin && git -C "$dest" reset --hard origin/main
      echo "  ✓ $label updated"
      return 0
    fi
  fi
  mkdir -p "$(dirname "$dest")"
  git clone --depth 1 "$REPO" "$dest"
  echo "  ✓ $label installed → $dest"
}

echo "Installing founder-playbook..."

# Detect package managers — install to every detected location for zero-config
if command -v opencode >/dev/null 2>&1 || [ -d "$HOME/.config/opencode" ]; then
  install_to "$HOME/.config/opencode/skills/founder-playbook" "OpenCode"
else
  # still install to opencode path if missing — harmless
  install_to "$HOME/.config/opencode/skills/founder-playbook" "OpenCode"
fi

if command -v claude >/dev/null 2>&1 || [ -d "$HOME/.claude" ]; then
  install_to "$HOME/.claude/skills/founder-playbook" "Claude Code"
else
  install_to "$HOME/.claude/skills/founder-playbook" "Claude Code"
fi

echo ""
echo "✓ Done. Restart your agent, then run:"
echo "  /founder-playbook"
echo "  /founder-playbook design my distribution for <product>"
echo ""
echo "Test: uv run python ~/.config/opencode/skills/founder-playbook/scripts/query_transcripts.py \"reddit first users\" --top 3"
