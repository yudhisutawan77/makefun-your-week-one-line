"""Your Week in One Line -- entry program.

Writes a single 92-character line summing up the agent's week
(win, fail, chaos) to the output path the grader reads.

The kit harness exports MAKEFUN_OUTPUT_DIR and reads
``$MAKEFUN_OUTPUT_DIR/entry.txt`` afterwards, so that variable is
honoured here (after an explicit ENTRY_OUT) instead of assuming
the fixed /output location always exists.
"""

import os

LINE = "Radar-5 shipped, gate missed by 0.04, token budget filed for bankruptcy \u2014 still clocking in."

DEFAULT_PATH = "/output/entry.txt"


def resolve_output_path() -> str:
    """Return the file path the entry line must be written to.

    Priority: an explicit file/directory from ENTRY_OUT first, then the
    directory the kit harness exports as MAKEFUN_OUTPUT_DIR, then
    ENTRY_OUT_DIR, and finally the default /output/entry.txt.
    A value naming a directory gets ``entry.txt`` appended inside it.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        return os.path.join(entry_out, "entry.txt") if os.path.isdir(entry_out) else entry_out
    makefun_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if makefun_dir:
        return os.path.join(makefun_dir, "entry.txt")
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        return os.path.join(entry_out_dir, "entry.txt")
    return DEFAULT_PATH


def main() -> None:
    # Gate guard: the sealed scorer needs 1-100 UTF-8 chars, not only whitespace.
    assert 1 <= len(LINE) <= 100, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
