# Reading and Writing Files in Python

> Sources: Real Python, James Mertz, 2019-02-20; Real Python, Leodanis Pozo Ramos, 2026-10-25
> Raw: [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md); [2026-10-31-realpython-python-with-statement](../../raw/python-file-io/2026-10-31-realpython-python-with-statement.md)
> Updated: 2026-10-31

## Overview

One of the most common tasks in Python is reading and writing files. Whether it's writing to a simple text file, reading a complicated server log, or analyzing raw byte data, all of these situations require reading or writing a file.

## Opening and Closing a File

To work with a file, open it with the `open()` built-in function. `open()` has a single required argument — the path to the file — and returns a file object:

```python
file = open('dog_breeds.txt')
```

You should always make sure that an open file is properly closed. It's your responsibility to close the file; upon termination of an application or script a file will be closed eventually, but there is no guarantee when. This can lead to unwanted behavior including resource leaks.

Two ways to ensure a file is closed properly, even on error:

1. `try-finally` block:

   ```python
   reader = open('dog_breeds.txt')
   try:
       # Further file processing goes here
   finally:
       reader.close()
   ```

2. `with` statement (recommended):

   ```python
   with open('dog_breeds.txt') as reader:
       # Further file processing goes here
   ```

The `with` statement automatically closes the file once it leaves the `with` block, even in cases of error, allowing cleaner code and easier handling of unexpected errors.

## File Modes

You can use the second positional argument, `mode`, a string representing how you want to open the file. The default and most common is `'r'`, which opens the file in read-only mode as a text file:

```python
with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here
```

Commonly used modes:

| Character | Meaning |
| --- | --- |
| `'r'` | Open for reading (default) |
| `'w'` | Open for writing, truncating (overwriting) the file first |
| `'rb'` or `'wb'` | Open in binary mode (read/write using byte data) |
| `'a'` | Append to the end of an already populated file |

## File Object Types

A file object is “an object exposing a file-oriented API (with methods such as `read()` or `write()`) to an underlying resource.” There are three categories, each defined in the `io` module:

- **Text files** — `open()` returns a `TextIOWrapper` file object (default).
- **Buffered binary files** — `open()` returns a `BufferedReader` or `BufferedWriter`.
- **Raw file types** — generally used as a low-level building block for binary and text streams; `open()` returns a `FileIO` file object (not typically used).

## Reading a File

| Method | What It Does |
| --- | --- |
| `.read(size=-1)` | Reads from the file based on the number of `size` bytes. No argument (or `None`/`-1`) reads the entire file. |
| `.readline(size=-1)` | Reads at most `size` characters from the line, continuing to end of line then wrapping around. |
| `.readlines()` | Reads the remaining lines and returns them as a list. |

Example — read the entire file:

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     print(reader.read())
Pug
Jack Russell Terrier
English Springer Spaniel
German Shepherd
Staffordshire Bull Terrier
Cavalier King Charles Spaniel
Golden Retriever
West Highland White Terrier
Boxer
Border Terrier
```

Iterating over each line — the more Pythonic and memory-efficient approach:

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     for line in reader:
>>>         print(line, end='')
```

## Writing a File

| Method | What It Does |
| --- | --- |
| `.write(string)` | Writes the string to the file. |
| `.writelines(seq)` | Writes the sequence to the file. No line endings are appended to each sequence item. |

Example — write breeds in reversed order:

```python
with open('dog_breeds.txt', 'r') as reader:
    dog_breeds = reader.readlines()

with open('dog_breeds_reversed.txt', 'w') as writer:
    for breed in reversed(dog_breeds):
        writer.write(breed)
```

## Working With Bytes

Working with files using byte strings is done by adding the `'b'` character to the `mode` argument. All of the same file-object methods apply, but each expects and returns a `bytes` object instead:

```python
>>> with open('dog_breeds.txt', 'rb') as reader:
>>>     print(reader.readline())
b'Pug\n'
```

A `.png` header is 8 bytes:

| Value | Interpretation |
| --- | --- |
| `0x89` | A “magic” number indicating the start of a PNG |
| `0x50 0x4E 0x47` | `PNG` in ASCII |
| `0x0D 0x0A` | A DOS style line ending `\r\n` |
| `0x1A` | A DOS style EOF character |
| `0x0A` | A Unix style line ending `\n` |

## See Also

- [File Concepts](file-concepts.md)
- [dos2unix Example](dos2unix-example.md)
- [Tips and Tricks](tips-tricks.md)
- [Standard Libraries](standard-libraries.md)
- [Vault Security](../data-archivist/vault-security.md)
- [Ancient Text Recovery](../data-archivist/ancient-text-recovery.md)
- [Context Managers and the with Statement](context-manager-with-statement.md)
