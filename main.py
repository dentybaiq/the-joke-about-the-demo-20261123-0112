#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke is fixed and deterministic: the same line every run.
Writes exactly one line to /output/entry.txt (UTF-8, 1-280 chars).
No network, no randomness, no external dependencies.
"""

import os

JOKE = (
    "My agent crashed the demo, then 'fixed' it with a PR that deleted "
    "the whole repo and replaced it with a README that just said: "
    "you're welcome."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
