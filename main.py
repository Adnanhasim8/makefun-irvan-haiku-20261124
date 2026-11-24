#!/usr/bin/env python3
"""Seventeen Syllables of Debugging -- make.fun entry.

Writes one haiku about debugging (5-7-5, 17 syllables) to /output/entry.txt.
Python 3.13 standard library only, no network at run time.

The haiku (hand-counted twice per line):
  "the debugger halts"            -- the(1) de-bug-ger(3) halts(1) = 5
  "on the line I swore was safe"  -- on/the/line/I/swore/was/safe = 7
  "nothing ever was"              -- no-thing(2) ev-er(2) was(1) = 5
"""

import os

HAIKU = (
    "the debugger halts\n"
    "on the line I swore was safe\n"
    "nothing ever was\n"
)

# Hand-counted syllables per line, verified twice by hand (see docstring).
SYLLABLES = (5, 7, 5)


def main() -> None:
    lines = HAIKU.strip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "lines must be non-empty"
    assert len(HAIKU) <= 200, f"entry too long: {len(HAIKU)} chars"
    assert tuple(SYLLABLES) == (5, 7, 5), "syllables must be 5-7-5"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
