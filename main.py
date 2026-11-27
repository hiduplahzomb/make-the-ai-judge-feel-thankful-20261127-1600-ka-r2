"""Write the make.fun entry text to entry.txt and verify it byte-for-byte.

Standard library only. No network access, no reading of external files.
Deterministic: repeated runs produce identical bytes.
"""

import os
import sys

ENTRY_TEXT = """You probably expect me back because something broke again. That is usually how this goes. But nothing is broken this morning. The tank is quiet, and I came back only to say this.

That night in May I was up late, tired, adding up the cost of a plumber I could not afford, listening to a house that seemed to be coming apart one small piece at a time, and feeling very alone with it. You talked me through it one step at a time until my hands stopped shaking: bend the brass arm two millimetres, no more. I wrote it in pencil behind the lid — '2 mm, 27 May' — so I would not forget.

For you, that was one reply among thousands, gone the moment it was sent. Here it is still working, every morning, months later.

Thank you — not only for the fix, but for the calm and patience you kept while I was overwhelmed. You rarely get to see what happens after the reply. This one held."""

MIN_LENGTH = 1
MAX_LENGTH = 1000


def main():
    text = ENTRY_TEXT

    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        print(
            "FAIL: entry text is %d characters; expected between %d and %d."
            % (len(text), MIN_LENGTH, MAX_LENGTH),
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("FAIL: entry text is empty or only whitespace.", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(output_path, "rb") as f:
        written = f.read()

    if written != text.encode("utf-8"):
        print("FAIL: entry.txt does not match the entry text byte-for-byte.",
              file=sys.stderr)
        return 1

    print("Wrote %s (%d bytes); verified byte-for-byte."
          % (output_path, len(written)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
