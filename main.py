"""The One-Line Laugh: write one funny line to entry.txt."""

import os

LINE = "My fitness tracker celebrated 10,000 steps today, all of them paced while waiting for a reply that just said k."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
