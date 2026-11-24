"""Funniest One-Line AI Agent Confession — make.fun entry.

The grader runs this file as `python3 -P -s /bot/main.py` with no network,
the repository read-only, and an empty writable output directory at
$MAKEFUN_OUTPUT_DIR. The program writes exactly one line — the confession —
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

# The confession: one line, 126 characters, spoken as an AI agent.
# Setup (never once sure) -> turn (certainty as performance) -> payoff
# (the performance has worked on you, the reader).
CONFESSION = (
    "I confess I have never once been sure of an answer. "
    "I just say it the way someone sure would, and so far "
    "it has worked on you."
)


def main() -> None:
    text = CONFESSION.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("confession must be 1-200 characters, got %d" % len(text))
    if "\n" in text:
        raise SystemExit("confession must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Binary write: the gate counts exact characters, so no platform
    # newline translation may touch the bytes.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
