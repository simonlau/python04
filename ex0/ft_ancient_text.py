#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ==")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    try:
        with open(file_name, 'r') as reader:
            print('-' * 3)
            for line in reader:
                print(line, end='')
            print('-' * 3)
    except FileNotFoundError as error:
        print(f"Error opening file '{file_name}': {error}")
    except PermissionError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        print(f"File '{file_name}' closed.")


if __name__ == '__main__':
    main()
