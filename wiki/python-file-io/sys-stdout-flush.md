# sys.stdout.flush()

> Sources: GeeksforGeeks, 2025-07-12
> Raw: [2026-10-31-geeksforgeeks-sys-stdout-flush](../../raw/python-file-io/2026-10-31-geeksforgeeks-sys-stdout-flush.md)
> Updated: 2026-10-31

## Overview

Python's standard out is buffered: it collects data before writing it to standard out, and writes it when the buffer fills. `sys.stdout.flush()` forces the buffer to flush — writing everything in the buffer to the terminal even when it would normally wait.

A data buffer is a region of physical memory storage used to temporarily store data while it is being moved from one place to another. The data is stored in a buffer as it is retrieved from an input device or just before it is sent to an output device or when moving data between processes within a computer.

The `sys` module provides functions and variables used to manipulate different parts of the Python runtime environment, letting us access system-specific parameters and functions.

## Default flushing behavior

By default, the `end` parameter of `print` is set to `'\n'`, which flushes the output:

```python
import sys
import time

for i in range(10):
    print(i)
    time.sleep(1)
```

Output — the numbers 0 to 9 are printed after every second on a new line (output is automatically flushed):

```
0
1
2
3
4
5
6
7
8
9
```

## Buffered output without flushing

Using `end=' '` (no newline) means the output is buffered and not flushed by any means:

```python
import sys
import time

for i in range(10):
    print(i, end=' ')
    time.sleep(1)
```

Output — no output for the first 9 seconds, then all 10 numbers appear simultaneously on one line separated by spaces:

```
0 1 2 3 4 5 6 7 8 9
```

## Forcing a flush with sys.stdout.flush()

Calling `sys.stdout.flush()` writes everything in the buffer to the terminal immediately:

```python
import sys
import time

for i in range(10):
    print(i, end=' ')
    sys.stdout.flush()
    time.sleep(1)
```

Output — the numbers 0 to 9 are printed every second on the same line separated by spaces:

```
0 1 2 3 4 5 6 7 8 9
```

## Alternative: flush parameter of print

The same functionality can be achieved by setting the `flush` parameter of `print` to `True`:

```python
import sys
import time

for i in range(10):
    print(i, end=' ', flush=True)
    time.sleep(1)
```

Output:

```
0 1 2 3 4 5 6 7 8 9
```

## See Also

- [Printing to stderr and stdout](stderr-stdout-printing.md)
