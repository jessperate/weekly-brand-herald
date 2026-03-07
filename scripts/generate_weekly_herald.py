#!/usr/bin/env python3
"""
Weekly Brand Herald Generator — Claude Code Edition

Instead of using API keys directly, this script invokes Claude Code
which uses your existing MCP connectors (Slack, Notion, Granola)
that are already authenticated in your Claude Desktop/Code setup.

Usage:
  # Manual run:
  claude -p "$(cat scripts/herald-prompt.md)" --cwd /path/to/weekly-brand-herald

  # Or via this wrapper:
  python scripts/generate_weekly_herald.py
"""

import subprocess
import sys
from pathlib import Path

REPO_DIR = Path(__file__).parent.parent
PROMPT_FILE = Path(__file__).parent / "herald-prompt.md"


def main():
    prompt = PROMPT_FILE.read_text()

    result = subprocess.run(
        ["claude", "-p", prompt, "--allowedTools", "mcp__claude_ai_Slack__*,mcp__claude_ai_Notion__*,mcp__claude_ai_Granola__*,Read,Write,Edit,Bash"],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
        timeout=600,
    )

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
