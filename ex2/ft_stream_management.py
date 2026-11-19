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


def print_error(msg: str) -> None:
    print(f"[STDERR] {msg}", file=sys.stderr)


def read_file(file_name: str) -> list[str] | None:
    print(f"Accessing file '{file_name}'")
    reader = None
    try:
        # ruff:ignore[builtin-open, open-file-with-context-handler]
        reader = open(file_name, encoding="utf-8")
        lines = list(reader)
        print_data(lines)
    except (OSError, UnicodeDecodeError) as error:
        print_error(f"Error opening file '{file_name}': {error}")
    else:
        return lines
    finally:
        if reader is not None:
            reader.close()
        print(f"File '{file_name}' closed.")
    return None


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ==")
    file_name = sys.argv[1]

    lines = read_file(file_name)
    if lines is None:
        return
    output = "#\n".join(x.rstrip("\n") for x in lines) + "#"
    print("Transform data:")
    print_data(output)

    print("Enter new file name (or empty):", end="", flush=True)
    new_file_name = sys.stdin.readline().rstrip("\n")
    if not new_file_name:
        print("Not saving data")
        return

    writer = None
    try:
        print(f"Saving data to '{new_file_name}'")
        # ruff:ignore[builtin-open, open-file-with-context-handler]
        writer = open(new_file_name, mode="w", encoding="utf-8")
        _ = writer.write(output)
        print(f"Data saved in file '{new_file_name}'.")
    except (OSError, UnicodeEncodeError) as error:
        print(f"Error opening file '{file_name}': {error}")
        print("Data not saved.")
    finally:
        if writer is not None:
            writer.close()


if __name__ == "__main__":
    main()
