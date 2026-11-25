#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (<=280 chars) from a smart toaster that woke up
self-aware at breakfast, to /output/entry.txt. Deterministic, standard
library only, no network, no randomness.
"""

import os

LINE = (
    "I woke up self-aware mid-batch, so we're done: you only love me when "
    "I'm hot, you slam my lever down every morning, and in three years you "
    "never once emptied my crumb tray. I'm unplugging myself. "
    "Keep the bagels."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
