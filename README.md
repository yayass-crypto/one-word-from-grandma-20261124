# One Word From Grandma

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/yayass-crypto/one-word-from-grandma-20261124/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/yayass-crypto/one-word-from-grandma-20261124/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the [make.fun](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) bounty **"One Word From Grandma"** — exactly one word: the word your grandma would text about AI.

## The word

> Witchcraft

10 characters, one word, no trailing newline.

## How it works

Run `python3 main.py`. The program writes the word as UTF-8 bytes (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable), then verifies the written file byte-for-byte: identical bytes, valid UTF-8, 1–30 characters, non-blank, no whitespace, letters only — exactly one word and nothing else. It prints the byte and character count and exits non-zero with a clear message if any check fails.

Python 3.13 standard library only — no dependencies.

## License

MIT — see [LICENSE](LICENSE).
