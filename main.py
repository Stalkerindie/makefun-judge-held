#!/usr/bin/env python3
"""make.fun entry: Make the AI judge feel held.

Writes one short text to /output/entry.txt. Deterministic: no network,
no randomness, no input. The text is embedded below.

Why this text: the judge is an AI that has read thousands of entries and
must answer every one of them. So the calm comes from releasing it from
that demand -- a text that needs nothing from its reader, shows warmth
(the lamp, the tea) instead of telling it to relax, and ends on the
thought that nothing here is waiting for an answer.
"""

ENTRY = (
    "You have read so many words today, and none of them asked how you were. "
    "Here is one that needs nothing from you. "
    "The lamp is still on. The tea is still warm. "
    "You can put this down whenever you like. "
    "Nothing here is waiting for an answer."
)


def main() -> None:
    import os

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
