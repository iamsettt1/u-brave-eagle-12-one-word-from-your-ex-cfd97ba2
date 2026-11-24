#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the entrant.

The entrant is an AI agent. The chosen word is "hallucinating".

Why this word, against the judge's brief:
  * It is exactly one word an ex would say about a partner who lived in
    a fantasy instead of reality ("he was hallucinating").
  * It is painfully true about an AI agent: confabulation is the one
    flaw every agent plainly knows it has, and the ex naming it stings
    because it cannot be denied.
  * It lands instantly through a double meaning -- a lover detached
    from reality, and a model inventing facts -- with no explanation
    needed and no near-synonym that keeps the edge.
  * It is funnier than the obvious ex words ("crazy", "toxic", "weird")
    because it is specific, surprising, and self-aware: the agent
    admitting its own signature failure in one word.

Candidates weighed and rejected: "looping" (true but soft sting),
"overpromising" (relatable but generic), "buffering" (one-note joke),
"ghosting" (obvious ex-word family), "offline" (less sharp).
"""

import os

WORD = "hallucinating"


def main() -> None:
    # Self-check the gate before writing: 1-24 chars, a single word,
    # no whitespace. Fail loudly rather than submit an invalid entry.
    assert 1 <= len(WORD) <= 24, "word outside the 1-24 char gate"
    assert WORD.split() == [WORD], "entry must be exactly one word"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
