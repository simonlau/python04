#!/usr/bin/env python3

import sys


def read_file(file_name: str) -> list[str] | None:
    print(f"Accessing file '{file_name}'")
    reader = None
    try:
        # ruff:ignore[builtin-open, open-file-with-context-handler]
        reader = open(file_name, encoding="utf-8")
        print("-" * 3)
        lines = list(reader)
        for line in lines:
            print(line, end="")
        print("-" * 3)
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    except UnicodeDecodeError as error:
        print(f"Error opening file '{file_name}': {error}")
    else:
        return lines
    finally:
        if reader is not None:
            reader.close()
        print(f"File '{file_name}' closed.")
    return None


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ==")
    file_name = sys.argv[1]

    lines = read_file(file_name)
    if lines is None:
        return
    lines = [line[:-1] + "#\n" for line in lines]
    print("Transform data:")
    print("-" * 3)
    for line in lines:
        print(line, end="")
    print("-" * 3)

    new_file_name = input("Enter new file name (or empty):").strip()
    if new_file_name == "":
        print("Not saving data")
        return

    writer = None
    try:
        print(f"Saving data to '{new_file_name}'")
        # ruff:ignore[builtin-open, open-file-with-context-handler]
        writer = open(new_file_name, mode="w", encoding="utf-8")
        print("-" * 3)
        writer.writelines(lines)
        print("-" * 3)
    except OSError as error:
        print(f"Error opening file '{new_file_name}': {error}")
    except UnicodeEncodeError as error:
        print(f"Error opening file '{new_file_name}': {error}")
    finally:
        if writer is not None:
            writer.close()
        print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
