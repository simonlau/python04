# Vault Security (Exercise 3)

> Sources: Data Archivist project (python04), 2026-10-30; Real Python, James Mertz, 2019-02-20
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md); [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md)
> Updated: 2026-10-30

## Overview

Vault Security operations where real archivists prove themselves. Create a secure_archive() function providing safe read/write access to any file using the with statement (context manager), which automatically closes files even on errors, preventing resource leaks.

## Requirements

- Use the with statement (introduced in this exercise; not allowed before).
- Implement secure_archive(file_name, action, content) where:
  - file_name is mandatory
  - action is an optional int or str indicating read or write
  - content is an optional string to write
- Returns a tuple (True|False, str): boolean success flag plus file contents or an error message.
- Code structure is reviewed during the defense.

## Authorized tools

open(), read(), write(), print()

## Closing files properly

You should always make sure that an open file is properly closed. There are two ways:

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

The `with` statement automatically closes the file once it leaves the `with` block, even in cases of error. It allows for cleaner code and makes handling unexpected errors easier.

## File object types

`open()` returns different file object types depending on mode:
- Text mode (`'r'`, `'w'`): `TextIOWrapper`
- Buffered binary mode (`'rb'`, `'wb'`): `BufferedReader` / `BufferedWriter`
- Raw binary mode (`'rb'`, buffering=0): `FileIO`

## See Also

- [Data Archivist Project Overview](data-archivist-overview.md)
- [Reading and Writing Files in Python](../python-file-io/reading-writing-files.md)
