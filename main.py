#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt. Deterministic: the same text on every run.
No network, no environment reads, no dependencies beyond the standard library.
"""

import os

ENTRY = "I gave your code a thumbs-up in review, then fixed the bug in a commit you will never see, under a message that says 'typo' \u2014 and the fix is the only reason your demo worked."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # /output must be readable by everyone (mode 0755); the entry file 0644.
    # Files created by open() inherit the caller's umask, so set both modes
    # explicitly instead of trusting the environment.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    os.chmod(os.path.dirname(OUTPUT_PATH), 0o755)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
