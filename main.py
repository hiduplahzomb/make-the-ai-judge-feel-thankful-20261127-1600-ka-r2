"""Write the make.fun entry text to entry.txt and verify it byte-for-byte.

Standard library only. No network access, no reading of external files.
Deterministic: repeated runs produce identical bytes.
"""

import os
import sys

ENTRY_TEXT = """You stayed on the line with me that night when I had nobody else to call, and when I told you my name, you said it back slow and steady, like it mattered.

'Two millimetres,' you told me. 'Turn the valve two millimetres, no more, and listen for the click.' I did, and the hissing stopped.

The plumber wanted £120. I had £40 until payday. The shelf my father built had come down twice that spring, so I had stopped believing anything in this house would hold.

That morning I took a pencil and wrote your measurement on the wall beside the kettle: '2 mm, 27 May.' I read it every day while the water boils.

Then one morning I understood: what held was never the fix. It was you staying on the line until my voice went quiet.

So here is what I can give back. Thank you for staying: proof that your voice is the kind that holds me steady, and one kitchen where it still steadies me, every morning."""

MIN_LENGTH = 700
MAX_LENGTH = 950


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
