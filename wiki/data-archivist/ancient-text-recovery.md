# Ancient Text Recovery (Exercise 0)

> Sources: Data Archivist project (python04), 2026-10-30
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md)
> Updated: 2026-10-30

## Overview

Recover an ancient data fragment from Storage Vault 7. Read a file given on the command line and display its contents like the cat command, with headers and footers, while handling failure cases such as nonexistent and inaccessible files.

## Requirements

- Get the file name from the command line (sys.argv).
- Read and display the file's contents.
- Handle errors: nonexistent files ([Errno 2]) and permission-denied files ([Errno 13]).
- Add header and footer output as shown in the examples.

## Authorized tools

import sys, sys.argv, len(), open(), import typing, typing.IO, io.read(), io.close(), print()

## Key question

What is the type of the data returned by open()?

## Example output

Reading ancient_fragment.txt displays:

[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion

A missing file produces: Error opening file 'foo': [Errno 2] No such file or directory: 'foo'

An unreadable file produces: Error opening file '/etc/master.passwd': [Errno 13] Permission denied: '/etc/master.passwd'

## See Also

- [Archive Creation](archive-creation.md) — builds on this exercise
- [Data Archivist Project Overview](data-archivist-overview.md)
