#!/usr/bin/env python3
"""One Word From Grandma — make.fun one-word entry.

Writes exactly one word (1-30 chars, no whitespace, no newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt, falling back
to out/entry.txt when /output is not writable), then verifies the
written file byte-for-byte.

Python 3.13 standard library only — no dependencies, no network.
"""

import os
import sys

WORD = "Witchcraft"

MAX_CHARS = 30


def output_dir() -> str:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    try:
        os.makedirs("/output", exist_ok=True)
        probe = "/output/.makefun-write-test"
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("ok")
        os.remove(probe)
        return "/output"
    except OSError:
        return "out"


def main() -> int:
    # Self-checks on the word before writing anything.
    if not WORD or not WORD.strip():
        print("error: word is empty or only whitespace", file=sys.stderr)
        return 1
    if WORD != WORD.strip():
        print("error: word has leading or trailing whitespace", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in WORD):
        print("error: entry is not exactly one word", file=sys.stderr)
        return 1
    if len(WORD) > MAX_CHARS:
        print(f"error: word is {len(WORD)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if not WORD.isalpha():
        print("error: word contains non-letters", file=sys.stderr)
        return 1

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = WORD.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Verify the written file byte-for-byte.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written bytes differ from the word", file=sys.stderr)
        return 1
    text = written.decode("utf-8")  # raises on invalid UTF-8
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        print("error: written text fails the 1-30 char gate", file=sys.stderr)
        return 1
    if text != WORD:
        print("error: written text is not exactly the word", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(data)} bytes, {len(text)} chars")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
