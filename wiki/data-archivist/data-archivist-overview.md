# Data Archivist Project Overview

> Sources: Data Archivist project (python04), 2026-10-30; Real Python, James Mertz, 2019-02-20
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md); [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md)
> Updated: 2026-10-30

## Overview

The Data Archivist project (version 3.0) is a Python file-operations exercise set in the year 2087, where data is humanity's greatest treasure and must be preserved against digital decay. The mission is to master file operations — opening, reading, writing, and error handling — so no knowledge is ever lost. The project consists of four progressive exercises plus submission guidelines.

## Scope

Topics covered:
- File operations: open, read, write, close
- Command-line arguments via sys.argv
- Error handling for nonexistent and inaccessible files
- The with statement (context manager), introduced in Exercise 3
- Standard streams: stdout, stderr, stdin
- Git-based submission

Related general Python file I/O concepts from Real Python: file paths, line endings (CR+LF vs LF), character encodings (ASCII, Unicode/UTF-8), file modes (`'r'`, `'w'`, `'rb'`, `'wb'`, `'a'`), file object types (`TextIOWrapper`, `BufferedReader`, `FileIO`), reading methods (`.read()`, `.readline()`, `.readlines()`), writing methods (`.write()`, `.writelines()`), and working with bytes.

## Rules

All programs must be written in Python 3.10 or later, comply with flake8, include type hints checked with mypy, handle exceptions gracefully, and be submitted to the assigned Git repository. Only repository content is evaluated.

The with statement is introduced in Exercise 3 and must not be used before then.

## Submission

Turn in the assignment to the assigned Git repository. Only work inside the repository is evaluated during the defense. Submit only the files requested by the project specification, using clean, simple code that clearly demonstrates understanding of file operations.

## See Also

- [AI Instructions](ai-instructions.md)
- [Ancient Text Recovery](ancient-text-recovery.md)
- [Archive Creation](archive-creation.md)
- [Stream Management](stream-management.md)
- [Vault Security](vault-security.md)
- [Reading and Writing Files in Python](../python-file-io/reading-writing-files.md)
