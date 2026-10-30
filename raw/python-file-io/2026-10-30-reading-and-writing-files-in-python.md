# Reading and Writing Files in Python (Guide)

> Source: https://realpython.com/read-write-files-python/
> Collected: 2026-10-30
> Published: 2019-02-20

## Overview

One of the most common tasks that you can do with Python is reading and writing files. Whether it’s writing to a simple text file, reading a complicated server log, or even analyzing raw byte data, all of these situations require reading or writing a file.

This tutorial is mainly for beginner to intermediate Pythonistas, but there are some tips in here that more advanced programmers may appreciate as well.

**In this tutorial, you’ll learn:**
- What makes up a file and why that’s important in Python
- The basics of reading and writing files in Python
- Some basic scenarios of reading and writing files

## What Is a File?

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary `1` and `0` for easier processing by the computer.

Files on most modern file systems are composed of three main parts:

1. **Header:** metadata about the contents of the file (file name, size, type, and so on)
2. **Data:** contents of the file as written by the creator or editor
3. **End of file (EOF):** special character that indicates the end of the file

What this data represents depends on the format specification used, which is typically represented by an extension. For example, a file that has an extension of `.gif` most likely conforms to the Graphics Interchange Format specification.

For this tutorial, you’ll only deal with `.txt` or `.csv` file extensions.

### File Paths

When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

1. **Folder Path:** the file folder location on the file system where subsequent folders are separated by a forward slash `/` (Unix) or backslash `\` (Windows)
2. **File Name:** the actual name of the file
3. **Extension:** the end of the file path pre-pended with a period (`.`) used to indicate the file type

Example file structure:

```
/
│
├── path/
|   │
|   ├── to/
|   │   └── cats.gif
|   │
|   └── dog_breeds.txt
|
└── animals.csv
```

The double-dot (`..`) can be chained together to traverse multiple directories above the current directory. For example, to access `animals.csv` from the `to` folder, you would use `../../animals.csv`.

### Line Endings

One problem often encountered when working with file data is the representation of a new line or line ending.

ASA standard states that line endings should use the sequence of the Carriage Return (`CR` or `\r`) *and* the Line Feed (`LF` or `\n`) characters (`CR+LF` or `\r\n`). The ISO standard however allowed for either the `CR+LF` characters or just the `LF` character.

Windows uses the `CR+LF` characters to indicate a new line, while Unix and the newer Mac versions use just the `LF` character. This can cause some complications when you’re processing files on an operating system that is different than the file’s source.

### Character Encodings

An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. The two most common encodings are ASCII and UNICODE. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values. It’s important to note that parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character. For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding, if there is a character that is outside of those 128 values, then an error will be thrown.

## Opening and Closing a File in Python

When you want to work with a file, the first thing to do is to open it. This is done by invoking the `open()` built-in function. `open()` has a single required argument that is the path to the file. `open()` has a single return, the file object:

```python
file = open('dog_breeds.txt')
```

**Warning:** You should *always* make sure that an open file is properly closed. It’s your responsibility to close the file. In most cases, upon termination of an application or script, a file will be closed eventually. However, there is no guarantee when exactly that will happen. This can lead to unwanted behavior including resource leaks.

When you’re manipulating a file, there are two ways that you can use to ensure that a file is closed properly, even when encountering an error:

The first way is to use the `try-finally` block:

```python
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()
```

The second way is to use the `with` statement:

```python
with open('dog_breeds.txt') as reader:
    # Further file processing goes here
```

The `with` statement automatically takes care of closing the file once it leaves the `with` block, even in cases of error. It is recommended to use the `with` statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier.

Most likely, you’ll also want to use the second positional argument, `mode`. This argument is a string that contains multiple characters to represent how you want to open the file. The default and most common is `'r'`, which represents opening the file in read-only mode as a text file:

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

A file object is “an object exposing a file-oriented API (with methods such as `read()` or `write()`) to an underlying resource.”

There are three different categories of file objects, each defined in the `io` module:

- Text files
- Buffered binary files
- Raw binary files

### Text File Types

A text file is the most common file that you’ll encounter:

```python
open('abc.txt')
open('abc.txt', 'r')
open('abc.txt', 'w')
```

With these types of files, `open()` will return a `TextIOWrapper` file object:

```python
>>> file = open('dog_breeds.txt')
>>> type(file)
<class '_io.TextIOWrapper'>
```

### Buffered Binary File Types

A buffered binary file type is used for reading and writing binary files:

```python
open('abc.txt', 'rb')
open('abc.txt', 'wb')
```

With these types of files, `open()` will return either a `BufferedReader` or `BufferedWriter` file object:

```python
>>> file = open('dog_breeds.txt', 'rb')
>>> type(file)
<class '_io.BufferedReader'>
>>> file = open('dog_breeds.txt', 'wb')
>>> type(file)
<class '_io.BufferedWriter'>
```

### Raw File Types

A raw file type is “generally used as a low-level building-block for binary and text streams.” It is therefore not typically used:

```python
open('abc.txt', 'rb', buffering=0)
```

With these types of files, `open()` will return a `FileIO` file object:

```python
>>> file = open('dog_breeds.txt', 'rb', buffering=0)
>>> type(file)
<class '_io.FileIO'>
```

## Reading and Writing Opened Files

Once you’ve opened up a file, you’ll want to read or write to the file.

| Method | What It Does |
| --- | --- |
| `.read(size=-1)` | Reads from the file based on the number of `size` bytes. If no argument is passed or `None` or `-1` is passed, then the entire file is read. |
| `.readline(size=-1)` | Reads at most `size` number of characters from the line. Continues to the end of the line and then wraps back around. |
| `.readlines()` | Reads the remaining lines from the file object and returns them as a list. |

Example — read the entire file using `.read()`:

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

Example — read 5 bytes of a line each time using `.readline()`:

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
Pug

Jack
Russe
ll Te
rrier
```

Example — read the entire file as a list using `.readlines()`:

```python
>>> f = open('dog_breeds.txt')
>>> f.readlines()
['Pug\n', 'Jack Russell Terrier\n', 'English Springer Spaniel\n', ...]
```

Iterating over each line — the more Pythonic, memory-efficient approach:

```python
>>> with open('dog_breeds.txt', 'r') as reader:
>>>     for line in reader:
>>>         print(line, end='')
```

Writing files — file objects have `.write()` and `.writelines()` methods:

| Method | What It Does |
| --- | --- |
| `.write(string)` | Writes the string to the file. |
| `.writelines(seq)` | Writes the sequence to the file. No line endings are appended to each sequence item. |

Example:

```python
with open('dog_breeds.txt', 'r') as reader:
    dog_breeds = reader.readlines()

with open('dog_breeds_reversed.txt', 'w') as writer:
    for breed in reversed(dog_breeds):
        writer.write(breed)
```

### Working With Bytes

Working with files using byte strings is done by adding the `'b'` character to the `mode` argument. All of the same methods for the file object apply. However, each of the methods expect and return a `bytes` object instead:

```python
>>> with open('dog_breeds.txt', 'rb') as reader:
>>>     print(reader.readline())
b'Pug\n'
```

A `.png` header is 8 bytes:

| Value | Interpretation |
| --- | --- |
| `0x89` | A “magic” number to indicate that this is the start of a `PNG` |
| `0x50 0x4E 0x47` | `PNG` in ASCII |
| `0x0D 0x0A` | A DOS style line ending `\r\n` |
| `0x1A` | A DOS style EOF character |
| `0x0A` | A Unix style line ending `\n` |

## A Full Example: `dos2unix.py`

A `dos2unix`-like tool that converts a file that contains line endings of `\r\n` to `\n`. Broken up into `str2unix()`, `dos2unix()`, and a `__main__` block.

```python
"""
A simple script and library to convert files or strings from dos like
line endings with Unix like line endings.
"""

import argparse
import os


def str2unix(input_str: str) -> str:
    r"""
    Converts the string from \r\n line endings to \n
    """
    r_str = input_str.replace('\r\n', '\n')
    return r_str


def dos2unix(source_file: str, dest_file: str):
    """
    Converts a file that contains Dos like line endings into Unix like
    """
    with open(source_file, 'r') as reader:
        dos_content = reader.read()

    unix_content = str2unix(dos_content)

    with open(dest_file, 'w') as writer:
        writer.write(unix_content)


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

## Tips and Tricks

### `__file__`

The `__file__` attribute is a special attribute of modules, similar to `__name__`. It is “the pathname of the file from which the module was loaded, if it was loaded from a file.” `__file__` returns the path *relative* to where the initial Python script was called.

### Appending to a File

Sometimes, you may want to append to a file or start writing at the end of an already populated file. This is easily done by using the `'a'` character for the `mode` argument:

```python
with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')
```

### Working With Two Files at the Same Time

You can read a file and write to another file at the same time:

```python
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
```

### Creating Your Own Context Manager

You may need finer control of the file object by placing it inside a custom class. Add `__enter__` and `__exit__` to create a context manager:

```python
class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()
```

## Don’t Re-Invent the Snake

Common file types can be handled using other modules. Two common file types you may need to work with are `.csv` and `.json`:

- Reading and Writing CSV Files in Python
- Working With JSON Data in Python

Built-in libraries:

- `wave`: read and write WAV files (audio)
- `aifc`: read and write AIFF and AIFC files
- `sunau`: read and write Sun AU files
- `tarfile`: read and write tar archive files
- `zipfile`: work with ZIP archives
- `configparser`: easily create and parse configuration files
- `xml.etree.ElementTree`: create or read XML based files
- `msilib`: read and write Microsoft Installer files
- `plistlib`: generate and parse Mac OS X `.plist` files

Popular third-party tools on PyPI:

- `PyPDF2`: PDF toolkit
- `xlwings`: read and write Excel files
- `Pillow`: image reading and manipulation

## You’re a File Wizard Harry

In this tutorial you’ve learned:
- What a file is
- How to open and close files properly
- How to read and write files
- Some advanced techniques when working with files
- Some libraries to work with common file types
