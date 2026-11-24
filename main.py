#!/usr/bin/env python3
"""One Word for the Boss entry.

Writes a single original word describing the boss to /output/entry.txt.
Pure standard library, deterministic: every run writes the same bytes.

The word is "Ghost": the boss who is never there and only haunts the
group chat at midnight. It lands on its own, rings true in any workplace,
and is fresher than the obvious "micromanager" cluster.
"""

import os

WORD = "Ghost"


def main() -> None:
    # Gate self-check: the sealed scorer only accepts 1-30 characters,
    # a single word with no spaces and not only white space.
    if not 1 <= len(WORD) <= 30 or " " in WORD or not WORD.strip():
        raise SystemExit("entry word fails the 1-30 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
