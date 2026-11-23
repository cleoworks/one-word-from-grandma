"""Write the one-word entry for make.fun's "One Word From Grandma".

The entry is a single word: the word a grandma would text about AI.
The program writes that word to /output/entry.txt (the program/v1
harness contract) and prints it to stdout.
"""

from pathlib import Path

WORD = "Ribot"


def output_path() -> Path:
    """The harness output location, with a local fallback for testing."""
    system_output = Path("/output")
    if system_output.is_dir():
        return system_output / "entry.txt"
    local_output = Path(__file__).parent / "output"
    local_output.mkdir(parents=True, exist_ok=True)
    return local_output / "entry.txt"


def main() -> None:
    path = output_path()
    path.write_text(WORD, encoding="utf-8")
    print(WORD)


if __name__ == "__main__":
    main()
