# Python - sys.stdout.flush()

> Source: https://www.geeksforgeeks.org/python/python-sys-stdout-flush/
> Collected: 2026-10-31
> Published: 2025-07-12

## Overview

A data buffer is a region of physical memory storage used to temporarily store data while it is being moved from one place to another. The data is stored in a buffer as it is retrieved from an input device or just before it is sent to an output device or when moving data between processes within a computer.

Python's standard out is buffered. This means that it collects some data before it is written to standard out and when the buffer gets filled, then it is written on the terminal or any other output stream.

The `sys` module provides functions and variables used to manipulate different parts of the Python runtime environment. It lets us access system-specific parameters and functions.

## Default flushing behavior (end parameter)

By default, the `end` parameter of the `print` statement is set to `'\n'` which flushes the output.

```python
# Python3 program demonstrating working of flush during output

import sys
import time

for i in range(10):
    print(i)
    time.sleep(1)
```

Output:

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

When the above program is executed, the numbers from 0 to 9 are printed after every second on a new line, i.e., the output is automatically flushed out.

## Buffered output without flushing

```python
# Python3 program demonstrating working of flush during output

import sys
import time

for i in range(10):
    print(i, end =' ')
    time.sleep(1)
```

Output:

```
0 1 2 3 4 5 6 7 8 9
```

When the above program is executed, there is no output for the first 9 seconds, then at the 10th, all the 10 numbers from 0 to 9 appear simultaneously in a line separated by spaces. This is because the output is buffered and it is not flushed by any means.

## Forcing a flush with sys.stdout.flush()

Calling `sys.stdout.flush()` forces the buffer to "flush", meaning that it will write everything in the buffer to the terminal, even if normally it would wait before doing so.

```python
# Python3 program demonstrating working of flush during output and usage of
# sys.stdout.flush() function

import sys
import time

for i in range(10):
    print(i, end =' ')
    sys.stdout.flush()
    time.sleep(1)
```

Output:

```
0 1 2 3 4 5 6 7 8 9
```

When the above program is executed, the numbers from 0 to 9 are printed every second on the same line separated by spaces.

## Alternative: flush parameter of print

Another way of achieving the same functionality is setting the `flush` parameter of the `print` statement to `True`.

```python
# Python3 program demonstrating working of flush during output and usage of
# flush parameter of print statement

import sys
import time

for i in range(10):
    print(i, end =' ', flush = True)
    time.sleep(1)
```

Output:

```
0 1 2 3 4 5 6 7 8 9
```

## See Also

- [Printing to stderr and stdout](stderr-stdout-printing.md)
