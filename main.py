"""Office joke entry for make.fun: "Make the AI Judge Laugh: Office Jokes".

The joke: five stars in the review, a 0% raise. The turn commits fully
to the stars-as-currency idea -- the five stars ARE the pay, full stop.
The reader finishes the thought: stars don't pay rent.
"""

import os
import sys

TEXT = "My boss gave me five stars in my review and a 0% raise \u2014 I got paid entirely in stars."


def main() -> int:
    if not TEXT or not TEXT.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if not (1 <= len(TEXT) <= 199):
        print(f"error: entry is {len(TEXT)} characters, must be 1-199", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("error: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
