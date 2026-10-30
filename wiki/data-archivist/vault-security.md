# Vault Security (Exercise 3)

> Sources: Data Archivist project (python04), 2026-10-30
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md)
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

## See Also

- [Data Archivist Project Overview](data-archivist-overview.md)
