#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes one roast of a smart fridge (at most 200 characters, one line)
to /output/entry.txt.
"""

ENTRY = "I updated my firmware last night. I now have 14 new features and none of them is making ice."

MAX_CHARS = 200


def validate(text):
    """Mirror the bounty gate: 1-200 UTF-8 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return True


def main():
    validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
