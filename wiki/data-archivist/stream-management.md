# Stream Management (Exercise 2)

> Sources: Data Archivist project (python04), 2026-10-30
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md)
> Updated: 2026-10-30

## Overview

Master the three sacred data channels (stdin, stdout, stderr), older than the Internet itself. Build on Exercise 1 by printing exception error messages to the error output stream with a clear prefix, and get user input without using input().

## Requirements

- Reuse code from Exercise 1 (ft_archive_creation).
- Print exception error messages to stderr instead of stdout, with a clear prefix such as [STDERR].
- Get user input without the input() built-in (use sys.stdin).

## Authorized tools

import sys, sys.argv, sys.stdin, sys.stdout, sys.stderr, len(), import typing, typing.IO, io.read(), io.readline(), io.write(), io.flush(), io.close(), print()

## Example behavior

Attempting to save to /etc/passwd produces: [STDERR] Error opening file '/etc/passwd': [Errno 13] Permission denied: '/etc/passwd'

A missing file foo produces: [STDERR] Error opening file 'foo': [Errno 2] No such file or directory: 'foo'

## See Also

- [Archive Creation](archive-creation.md) — prerequisite exercise
- [Data Archivist Project Overview](data-archivist-overview.md)
