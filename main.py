#!/usr/bin/env python3
"""A Day of One-Line Pitches — u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one sentence (at most 240 characters) to /output/entry.txt: a pitch
that would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun. Standard library only.
"""

import os

PITCH = (
    "Tell an AI agent the app idea you've been carrying in your head for "
    "months, and watch it build a working first version while you finish "
    "your coffee \u2014 no code, no setup, just your idea finally real."
)


def main() -> None:
    text = PITCH.strip()
    assert text, "pitch must not be blank"
    assert len(text) <= 240, f"pitch is {len(text)} chars, over the 240 cap"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
