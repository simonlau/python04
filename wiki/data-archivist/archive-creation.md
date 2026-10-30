# Archive Creation (Exercise 1)

> Sources: Data Archivist project (python04), 2026-10-30; Real Python, James Mertz, 2019-02-20
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md); [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md)
> Updated: 2026-10-30

## Overview

Establish a preservation protocol by creating fresh archive entries, building on Exercise 0. Add a special archive character (#) at the end of each line (2087-compatible), display the transformed content, prompt the user for a save file name (empty to skip saving), and save when a name is provided.

## Requirements

- Reuse code from Exercise 0 (ft_ancient_text).
- Append # to the end of each line.
- Display the new content.
- Ask the user for a file name to save to; empty means do not save.
- Create or replace the target file if a name is given.
- Show a saving confirmation message.

## Authorized tools

import sys, sys.argv, len(), open(), import typing, typing.IO, io.read(), io.write(), io.close(), print(), input()

## Writing details

- `.write(string)` — writes the string to the file.
- `.writelines(seq)` — writes the sequence to the file; no line endings are appended to each item.
- Mode `'w'` opens for writing, truncating (overwriting) the file first.
- Mode `'a'` appends to the end of an already populated file (useful for adding archive entries without overwriting).

## See Also

- [Ancient Text Recovery](ancient-text-recovery.md) — prerequisite exercise
- [Data Archivist Project Overview](data-archivist-overview.md)
- [Reading and Writing Files in Python](../python-file-io/reading-writing-files.md)
