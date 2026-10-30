# File Concepts

> Sources: Real Python, James Mertz, 2019-02-20
> Raw: [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md)
> Updated: 2026-10-30

## Overview

Before working with files in Python, it helps to understand what a file is, how file paths are structured, and the common pitfalls of line endings and character encodings.

## What Is a File?

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are translated into binary `1` and `0` for easier processing by the computer.

Files on most modern file systems are composed of three main parts:

1. **Header:** metadata about the contents of the file (file name, size, type, and so on)
2. **Data:** contents of the file as written by the creator or editor
3. **End of file (EOF):** special character that indicates the end of the file

What this data represents depends on the format specification used, which is typically represented by an extension. For example, a file with a `.gif` extension most likely conforms to the Graphics Interchange Format specification.

## File Paths

When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It's broken up into three major parts:

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

## Line Endings

One problem often encountered when working with file data is the representation of a new line or line ending.

The ASA standard states that line endings should use the sequence of the Carriage Return (`CR` or `\r`) *and* the Line Feed (`LF` or `\n`) characters (`CR+LF` or `\r\n`). The ISO standard allowed for either the `CR+LF` characters or just the `LF` character.

Windows uses the `CR+LF` characters to indicate a new line, while Unix and newer Mac versions use just the `LF` character. This can cause complications when processing files on an operating system different from the file's source, and may make iterating over each line problematic.

## Character Encodings

An encoding is a translation from byte data to human-readable characters, typically by assigning a numerical value to represent a character. The two most common encodings are ASCII and Unicode. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical-to-character values. Parsing a file with the incorrect character encoding can lead to failures or misrepresentation of characters. For example, if a file was created using UTF-8 and you try to parse it using ASCII, a character outside the 128 ASCII values will throw an error.

## See Also

- [Reading and Writing Files in Python](reading-writing-files.md)
- [Data Archivist Project Overview](../data-archivist/data-archivist-overview.md)
