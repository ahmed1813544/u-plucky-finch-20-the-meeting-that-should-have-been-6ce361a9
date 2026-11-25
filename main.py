"""The Meeting That Should Have Been an Email — entry.

Writes exactly one line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set): a single
joke about a meeting that should have been an email, at most 200
characters, no trailing newline, so the file holds the joke alone.
Standard library only; the output never changes between runs.
"""

import os

LINE = (
    "Forty people joined the meeting to protect one fragile sentence "
    "\u2014 'still working on it' \u2014 which had already been emailed, "
    "read, and answered before anyone sat down."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
