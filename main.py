# SPDX-License-Identifier: MIT
"""Museum of the Year 3000 — one-line museum label entry.

This program writes a single museum label, the kind that would sit
beside an ordinary object in a museum three thousand years from now.
The object chosen here is the group chat: the most crowded room of
the 2020s, where everybody talked and nobody decided anything.
"""

# Why the group chat, and not the plastic fork or the parking meter?
# A fork is silent; a meter is patient. A group chat is the only
# everyday object that performs its own absurdity in public: dozens
# of adults, one simple question, and a scroll of replies that
# answers everything except the question itself. The museum label
# works because it treats that noise with total curatorial calm —
# "c. 2026", as if future historians had already given up too.

ENTRY = (
    "The Group Chat, c. 2026. One question was asked. "
    "Nobody answered it. Four hundred messages later, "
    "dinner is still undecided."
)

# The label is deliberately flat and factual, in the voice of a
# plaque on a wall. The joke lives in the gap between the formal
# museum tone and the very familiar failure it describes: everyone
# has been in that chat, watching dinner drift further away with
# every cheerful, irrelevant reply.

MAX_CHARS = 200


def validate(entry):
    """A museum label must be exactly one line, at most 200 chars."""
    lines = entry.splitlines()
    if len(lines) != 1:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    return entry


def write_entry(entry, path="/output/entry.txt"):
    """Write the validated label to the harness output file."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    return path


def main():
    label = validate(ENTRY)
    print(label)
    write_entry(label)


if __name__ == "__main__":
    main()
