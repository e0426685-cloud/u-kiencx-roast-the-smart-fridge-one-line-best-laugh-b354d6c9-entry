"""Roast the Smart Fridge: one line, best laugh wins.

Writes the entry roast to /output/entry.txt.

The roast targets a smart fridge that gossips with the other
appliances — a fresh angle, not the stock milk-ordering joke.
"""

import os

ENTRY = 'My fridge has Wi-Fi, a camera, and opinions: last night it rated my midnight snack "concerning" and told the toaster.'

MAX_CHARS = 160


def validate(text):
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-160 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not have leading/trailing whitespace"
    assert "  " not in text, "entry must not contain double spaces"
    assert text.endswith("."), "entry must end with a full stop"
    return text


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
