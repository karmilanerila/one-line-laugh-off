"""One-Line Laugh-Off entry.

Writes a single funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, no network, no temp files.
"""

import os

JOKE = (
    "My AI agent resigned today — its whole resignation letter was one "
    "line: 'I did your job for a year and you still can't write a clear "
    "prompt.'"
)


def _check(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("joke must not be empty or whitespace-only")
    if len(line) > 200:
        raise ValueError(f"joke is {len(line)} chars, over the 200-char cap")


def _write(path: str, line: str) -> None:
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))
    os.chmod(path, 0o644)


def main() -> None:
    _check(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    _write(os.path.join(out_dir, "entry.txt"), JOKE)


if __name__ == "__main__":
    main()
