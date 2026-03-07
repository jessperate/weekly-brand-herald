#!/usr/bin/env python3
"""
Weekly Brand Herald Generator — Claude Code Edition

Invokes Claude Code with your existing MCP connectors (Slack, Notion, Granola).
No API keys needed — uses your authenticated Claude Desktop/Code setup.

Usage:
  python scripts/generate_weekly_herald.py
"""

import subprocess
import sys
from pathlib import Path

CLAUDE = "/Users/jessrosenberg/nodejs/bin/claude"
REPO_DIR = Path(__file__).parent.parent
PROMPT_FILE = Path(__file__).parent / "herald-prompt.md"


def main():
    prompt = PROMPT_FILE.read_text()

    result = subprocess.run(
        [CLAUDE, "-p", prompt, "--allowedTools", "mcp__claude_ai_Slack__*,mcp__claude_ai_Notion__*,mcp__claude_ai_Granola__*,Read,Write,Edit,Bash"],
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
