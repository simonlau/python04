#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ==")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    reader = None
    num_dashes = 3
    try:
        # ruff:ignore[builtin-open, open-file-with-context-handler]
        reader = open(file_name, encoding="utf-8")
        print("-" * num_dashes)
        for line in reader:
            print(line, end="")
        print("-" * num_dashes)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if reader is not None:
            reader.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
