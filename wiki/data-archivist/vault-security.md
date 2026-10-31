# Vault Security (Exercise 3)

> Sources: Data Archivist project (python04), 2026-10-30; Real Python, James Mertz, 2019-02-20; Real Python, Leodanis Pozo Ramos, 2026-10-25
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md); [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md); [2026-10-31-realpython-python-with-statement](../../raw/python-file-io/2026-10-31-realpython-python-with-statement.md)
> Updated: 2026-10-31

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

## Context Manager Protocol

Python's `with` statement creates a runtime context that allows you to execute a code block under the control of a context manager. PEP 343 added the `with` statement to factor out common use cases of the `try ... finally` construct.

A context manager is an object that implements two special methods:

- `.__enter__(self)` — called when entering the runtime context; handles setup logic; its return value is bound to the `with` target variable (if `as obj` is given).
- `.__exit__(self, exc_type, exc_value, exc_tb)` — called when leaving the `with` block; handles teardown logic; if an exception occurs, `exc_type`, `exc_value`, and `exc_tb` hold the exception type, value, and traceback.

Here's how the `with` statement works internally:

1. Execute the expression after `with` to obtain a context manager object.
2. Call `.__enter__()` and bind its return value to the target variable.
3. Execute the `with` code block.
4. Call `.__exit__()` when the block finishes, even if an exception occurred.

`open()` returns an `io.TextIOBase` object that supports this protocol, so `with open(...) as file:` automatically closes the file when the block ends.

You can also supply multiple context managers separated by commas, which works like nested `with` statements without nesting:

```python
with open("hello.txt") as in_file, open("output.txt", "w") as out_file:
    for line in in_file:
        out_file.write(line.upper())
```

The `with` statement is less generic than `try ... finally` (it only works with objects that support the context management protocol), but it's clearer, safer, and more readable, and it makes it almost impossible to forget to clean up, close, and release resources.

## File object types

`open()` returns different file object types depending on mode:
- Text mode (`'r'`, `'w'`): `TextIOWrapper`
- Buffered binary mode (`'rb'`, `'wb'`): `BufferedReader` / `BufferedWriter`
- Raw binary mode (`'rb'`, buffering=0): `FileIO`

## See Also

- [Data Archivist Project Overview](data-archivist-overview.md)
- [Reading and Writing Files in Python](../python-file-io/reading-writing-files.md)
- [Context Managers and the with Statement](../python-file-io/context-manager-with-statement.md)
