#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. Deterministic: no randomness, no network, no input,
stdlib only. Running it twice produces the exact same file.
"""

import os

LINE = (
    "My daughter's drawing of our family had four figures, and when I asked "
    "who the fifth one standing behind me was, she whispered, \"That's you, "
    "Daddy - the one who came home yesterday.\""
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not text:
        raise ValueError("entry line must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over {MAX_CHARS}")
    if text.rstrip("\"'")[-1] not in ".!?":
        raise ValueError("entry must end with sentence punctuation")
    if text.count(".") > 1:
        raise ValueError("entry must be a single sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
