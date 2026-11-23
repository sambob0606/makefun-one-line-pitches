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
    if not text:
        raise SystemExit("error: pitch must not be blank")
    if len(text) > 240:
        raise SystemExit(
            f"error: pitch is {len(text)} chars, over the 240-char cap"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("error: pitch must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        with open(out_path, encoding="utf-8") as f:
            if f.read() != text:
                raise SystemExit(
                    f"error: wrote {out_path} but contents do not match"
                )
    except OSError as exc:
        raise SystemExit(f"error: cannot write entry to {out_path}: {exc}")
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
