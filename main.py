#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to /output/entry.txt: a joke that hints
at a whole story in the few words a passer-by sees in a phone's list.
"""

import os

STORY = "My ex kept the dog AND the WiFi"


def validate(text: str) -> str:
    """Enforce the bounty gate: 1 to 32 characters, not only whitespace."""
    if not 1 <= len(text) <= 32:
        raise ValueError(f"story must be 1-32 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(STORY))


if __name__ == "__main__":
    main()
