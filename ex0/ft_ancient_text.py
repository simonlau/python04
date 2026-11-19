#!/usr/bin/env python3

import sys
from collections.abc import Iterable


def print_data(data: Iterable[str]) -> None:
    num_dashes = 3
    print("-" * num_dashes)
    print()
    for line in data:
        print(line, end="")
    print()
    print("-" * num_dashes)


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ==")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    reader = None
    try:
        # ruff:ignore[builtin-open, open-file-with-context-handler]
        reader = open(file_name, encoding="utf-8")
        print_data(reader)
        print(f"File '{file_name}' closed.")
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if reader is not None:
            reader.close()


if __name__ == "__main__":
    main()
