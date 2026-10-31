# Printing to stderr and stdout

> Sources: GeeksforGeeks, 2025-07-12
> Raw: [2026-10-31-geeksforgeeks-print-stderr-stdout](../../raw/python-file-io/2026-10-31-geeksforgeeks-print-stderr-stdout.md)
> Updated: 2026-10-31

## Overview

In Python, `print()` writes text to `sys.stdout`, `input()` reads from `sys.stdin`, and exceptions are written to `sys.stderr`. Output can be redirected to a stream other than stdout — for example, to keep a log of output or to suppress console output.

## Standard streams

| Stream | Purpose |
| --- | --- |
| `sys.stdout` | Standard output — receives regular program information; `print()` writes here by default |
| `sys.stderr` | Standard error — receives error information; exceptions are written here |
| `sys.stdin` | Standard input — `input()` reads from here |

## Printing to stderr

`sys.stderr` is comparable to `sys.stdout` in that it prints straight to the console, but it prints only exceptions and error messages.

### Method 1: `print(..., file=sys.stderr)`

```python
import sys

def print_to_stderr(*a):
    # a is the array holding the objects passed as the argument
    print(*a, file=sys.stderr)

print_to_stderr("Hello World")
```

### Method 2: `sys.stderr.write()`

Accomplishes the same task as the stream it stands for; in interactive mode it also reports the text's letter count.

```python
import sys

print("Example 1")
print("Example 2", file=sys.stderr)
sys.stderr.write("Example 3")
```

### Method 3: `logging.warning`

A built-in Python package tool that enables publishing status messages to files or other output streams.

```python
import logging

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
log.warning('Error: Hello World')
print('GeeksforGeeks')
```

Output:

```
Error: Hello World
GeeksforGeeks
```

## Printing to stdout

### Method 1: `print(..., file=sys.stdout)`

```python
import sys

def print_to_stdout(*a):
    print(*a, file=sys.stdout)

print_to_stdout("Hello World")
```

### Method 2: `print()`

```python
print( "Hello GeeksforGeeks" )
```

Output:

```
Hello GeeksforGeeks
```

### Method 3: `sys.stdout.write()`

Serves the same purpose as the stream; in interactive mode it also reports the number of letters within the text.

```python
import sys

a = 11

print(a)
print(a, file=sys.stdout)
sys.stdout.write(a)
```

## See Also

- [Reading and Writing Files in Python](reading-writing-files.md)
- [Stream Management](../data-archivist/stream-management.md)
