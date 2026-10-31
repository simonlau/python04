#!/usr/bin/env python3

import sys


def read_file(file_name: str) -> list[str] | None:
    print(f"Accessing file '{file_name}'")
    try:
        with open(file_name, mode="r", encoding="utf-8") as reader:
            print("-" * 3)
            lines = [line for line in reader]
            for line in lines:
                print(line, end="")
            print("-" * 3)
            return lines
    except FileNotFoundError as error:
        print(f"Error opening file '{file_name}': {error}")
    except PermissionError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
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

    try:
        print(f"Saving data to '{new_file_name}'")
        with open(new_file_name, "w") as writer:
            print("-" * 3)
            writer.writelines(lines)
            print("-" * 3)
    except PermissionError as error:
        print(f"Error opening file '{new_file_name}': {error}")
    finally:
        print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
