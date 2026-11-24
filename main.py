#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (1-320 chars) to /output/entry.txt.
"""

import os

LINE = (
    "The committee drafting the law that will govern artificial intelligence "
    "just emailed IT a screenshot of a Word document and asked them to turn "
    "it into a PDF."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 320, f"entry length {len(text)} out of range"
    assert text.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
