# Archive Creation (Exercise 1)

> Sources: Data Archivist project (python04), 2026-10-30
> Raw: [2026-10-30-data-archivist-python04](../../raw/data-archivist/2026-10-30-data-archivist-python04.md)
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

## See Also

- [Ancient Text Recovery](ancient-text-recovery.md) — prerequisite exercise
- [Data Archivist Project Overview](data-archivist-overview.md)
