# dos2unix Example

> Sources: Real Python, James Mertz, 2019-02-20
> Raw: [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md)
> Updated: 2026-10-30

## Overview

A `dos2unix`-like tool that converts a file containing `\r\n` line endings to `\n`. It's broken up into `str2unix()`, `dos2unix()`, and a `__main__` block that runs only when the file is executed as a script.

## str2unix()

Converts a string from `\r\n` line endings to `\n`:

```python
def str2unix(input_str: str) -> str:
    r"""
    Converts the string from \r\n line endings to \n
    """
    r_str = input_str.replace('\r\n', '\n')
    return r_str
```

## dos2unix()

Converts a file that contains DOS-like line endings into Unix-like:

```python
def dos2unix(source_file: str, dest_file: str):
    """
    Converts a file that contains Dos like line endings into Unix like
    """
    with open(source_file, 'r') as reader:
        dos_content = reader.read()

    unix_content = str2unix(dos_content)

    with open(dest_file, 'w') as writer:
        writer.write(unix_content)
```

## __main__ block

Uses `argparse` to accept a `source_file` argument and an optional `--dest_file`. When no destination is given, it creates a new file based on the source name with `_unix` appended before the extension:

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that converts a DOS like file to an Unix like file",
    )
    parser.add_argument(
        'source_file',
        help='The location of the source '
    )
    parser.add_argument(
        '--dest_file',
        help='Location of dest file (default: source_file appended with `_unix`',
        default=None
    )
    args = parser.parse_args()
    s_file = args.source_file
    d_file = args.dest_file

    if d_file is None:
        file_path, file_extension = os.path.splitext(s_file)
        d_file = f'{file_path}_unix{file_extension}'

    dos2unix(s_file, d_file)
```

## See Also

- [Reading and Writing Files in Python](reading-writing-files.md)
