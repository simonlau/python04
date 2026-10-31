# Context Managers and the with Statement

> Sources: Real Python, Leodanis Pozo Ramos, 2026-10-25
> Raw: [2026-10-31-realpython-python-with-statement](../../raw/python-file-io/2026-10-31-realpython-python-with-statement.md)
> Updated: 2026-10-31

## Overview

Python's `with` statement allows you to manage external resources safely by using objects that support the context manager protocol. These objects automatically handle the setup and teardown phases of common operations.

By using the `with` statement alongside appropriate context managers, you can focus on your core logic while the context managers prevent resource leaks like unclosed files, unreleased memory, or dangling network connections.

Key points:

- Python's `with` statement automates the process of setting up and tearing down computational resources using context managers.
- Using `with` reduces code complexity and prevents resource leaks by ensuring proper resource release, even if exceptions occur.
- A context manager in Python is an object that implements `.__enter__()` and `.__exit__()` methods to manage resources safely.

## Managing External Resources in Python

Properly managing external resources, such as files, locks, and network connections, is a common requirement in programming. Sometimes, a program uses a given resource and doesn't release the associated memory when it no longer needs the resource. This kind of issue is called a memory leak because the available memory shrinks every time you create a new instance of a resource without releasing the unneeded ones.

Managing resources properly requires setup and teardown phases. The latter phase requires cleanup actions, like closing a file, releasing a lock, or closing a network connection. If you forget to perform these cleanup actions, then your application keeps the resource occupied, which might compromise valuable system resources, such as memory and network bandwidth.

Writing text to files is usually a buffered operation. Calling `.write()` on a file won't immediately result in writing text to the physical file, but to a temporary buffer. Sometimes, when the buffer isn't full, developers forget to call `.close()` and part of the data can be lost.

Another possibility is that your application runs into errors or exceptions that cause the control flow to bypass the code responsible for releasing the resource at hand.

## `try ... finally` vs `with`

In Python, you can use two general approaches to deal with resource management:

1. A `try ... finally` construct
2. A `with` construct

The `try ... finally` construct is generic and allows you to provide setup and teardown code to manage any kind of resource. However, it's verbose, and you might forget some cleanup actions if you use it in several places:

```python
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
finally:
    file.close()
```

The `with` construct provides a straightforward way to provide and reuse setup and teardown code. Its limitation is that it only works with objects that support the context management protocol:

```python
with open("hello.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World!")
```

When you run this `with` statement, `open()` returns an `io.TextIOBase` object. This object supports the context manager protocol, so the `with` statement calls `.__enter__()` and assigns its return value to `file`. Then, you can manipulate the file inside the `with` code block. When the block ends, Python automatically calls `.__exit__()`, which closes the file for you, even if an exception occurs in the `with` code block.

## The `with` Statement

The Python `with` statement creates a runtime context that allows you to execute a code block under the control of a context manager. PEP 343 added the `with` statement to make it possible to factor out common use cases of the `try ... finally` construct.

Compared to the traditional `try ... finally` construct, the `with` statement makes your code clearer, safer, and more readable. Many classes and objects in the standard library support the `with` statement by implementing the context manager protocol.

To write a `with` statement, use the following general syntax:

```python
with expression [as obj]:
    <block>
```

The `expression` after `with` must return an object that implements the context management protocol, which consists of two special methods:

1. `.__enter__()` is called by the `with` statement to enter the runtime context.
2. `.__exit__()` is called when the execution leaves the `with` code block.

The `as` specifier is optional. If you provide an `obj` variable with `as`, then the return value of calling `.__enter__()` on the context manager object is bound to that variable.

Note: Some context managers return `None` from `.__enter__()` because they have no useful object to give back to the caller. In these situations, specifying an `obj` variable makes no sense.

Here's how the `with` statement works internally:

1. Execute `expression` to obtain a context manager object.
2. Call `.__enter__()` on the context manager and bind its return value to `obj` if provided.
3. Execute the `with` code block.
4. Call `.__exit__()` on the context manager when the `with` code block finishes.

The `.__enter__()` method typically provides the setup logic. The `.__exit__()` method typically provides the teardown logic or cleanup code, such as calling `.close()` on an open file object.

The `with` statement also supports multiple context managers separated by commas, which works like nested `with` statements but without nesting:

```python
with open("hello.txt") as in_file, open("output.txt", "w") as out_file:
    for line in in_file:
        out_file.write(line.upper())
```

The `with` statement helps avoid resource leaks by making it almost impossible to forget to clean up, close, and release resources after you're done with them.

## Common Uses of `with`

### Working With Files

Managing files with `with` is generally recommended because it ensures that opened file descriptors are automatically closed after the flow of execution leaves the `with` code block:

```python
with open("hello.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World!")
```

A common mistake is to reuse an already closed file object in a second `with`:

```python
>>> file = open("hello.txt", mode="w", encoding="utf-8")
>>> with file:
...     file.write("Hello, World!")
...
13
>>> with file:
...     file.write("Welcome to Real Python!")
...
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
```

Another way to use `with` to open and manage files is by using the `.open()` method on a `pathlib.Path` object:

```python
>>> import pathlib
>>> file_path = pathlib.Path("hello.txt")
>>> with file_path.open("w", encoding="utf-8") as file:
...     file.write("Hello, World!")
...
13
```

Whenever you load an external file, check for possible issues such as a missing file, writing and reading access, and so on:

```python
>>> import pathlib
>>> import logging
>>> file_path = pathlib.Path("/hello.txt")
>>> try:
...     with file_path.open(mode="w") as file:
...         file.write("Hello, World!")
... except OSError as error:
...     logging.error("Writing to file %s failed due to: %s", file_path, error)
...
ERROR:root:Writing to file /hello.txt failed due to: [Errno 13] Permission denied: '/hello.txt'
```

### Traversing Directories

The `os` module provides `scandir()`, which returns an iterator over `os.DirEntry` objects corresponding to the entries in a given directory. The iterator supports the context management protocol:

```python
>>> import os
>>> with os.scandir(".") as entries:
...     for entry in entries:
...         print(entry.name, "->", entry.stat().st_size, "bytes")
...
Documents -> 4096 bytes
Videos -> 12288 bytes
Desktop -> 4096 bytes
DevSpace -> 4096 bytes
.profile -> 807 bytes
Templates -> 4096 bytes
Pictures -> 12288 bytes
Public -> 4096 bytes
Downloads -> 4096 bytes
```

When the `with` block finishes, `.__exit__()` calls `scandir.close()` to close the iterator and release the acquired resources.

### Performing High-Precision Calculations

The `decimal` module provides `localcontext()` to tweak the precision used in a calculation involving decimal numbers. The precision defaults to 28 places:

```python
>>> from decimal import Decimal, localcontext
>>> with localcontext(prec=42):
...     Decimal("1") / Decimal("42")
...
Decimal('0.0238095238095238095238095238095238095238095')
>>> Decimal("1") / Decimal("42")
Decimal('0.02380952380952380952380952381')
```

When the `with` code block finishes, the precision is back to its default value of 28 places.

### Handling Locks in Multithreaded Programs

The `threading.Lock` class supports the `with` statement to automatically acquire and release a lock:

```python
import threading

balance_lock = threading.Lock()

# Use the try ... finally pattern
balance_lock.acquire()
try:
    # Update the account balance here ...
finally:
    balance_lock.release()

# Use the with pattern
with balance_lock:
    # Update the account balance here ...
```

The `with` statement automatically acquires and releases a lock when the flow of execution enters and leaves the statement, creating a protected region known as the critical section.

### Testing for Exceptions With pytest

`pytest.raises()` returns a context manager, so you can use it in a `with` statement to assert that a block of code raises a specific exception:

```python
>>> import pytest
>>> with pytest.raises(ZeroDivisionError):
...     1 / 0
...
>>> favorites = {"fruit": "apple", "pet": "dog"}
>>> with pytest.raises(KeyError):
...     favorites["car"]
...
```

You can also specify a target variable to inspect the raised exception:

```python
>>> with pytest.raises(ZeroDivisionError) as exc:
...     1 / 0
...
>>> assert str(exc.value) == "division by zero"
```

## Advantages of the `with` Statement

- Makes resource management safer than using equivalent `try ... finally` constructs.
- Encapsulates standard uses of `try ... finally` constructs in context managers.
- Allows using context managers to pack the code that handles setup and teardown logic.
- Helps prevent resource leaks.

## Using the `async with` Statement

The `with` statement also has an asynchronous version, `async with`, for context managers that work within asynchronous code. It's common to see `async with` in I/O-bound code, which involves setup and teardown phases.

```python
import asyncio
import aiohttp

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"{url}: type -> {html[:17].strip()}")
```

The `async with` statement works like a regular `with` statement, but it requires an asynchronous context manager that implements `.__aenter__()` and `.__aexit__()` (the asynchronous counterparts to `.__enter__()` and `.__exit__()`). When you use `async with ctx_mgr`, Python implicitly calls `await ctx_mgr.__aenter__()` on entry and `await ctx_mgr.__aexit__()` on exit.

## Creating Custom Context Managers

There's nothing special about `open()`, `threading.Lock`, `decimal.localcontext()`, and the others. They simply return objects that implement the context management protocol.

You can provide the same functionality by implementing `.__enter__()` and `.__exit__()` special methods in class-based context managers, or by using the `contextlib.contextmanager` decorator with a generator function for function-based context managers.

Context managers and the `with` statement aren't limited to resource management. They allow you to provide and reuse common setup and teardown code for any pair of operations that must occur before and after a task, such as:

- Open and close
- Lock and release
- Change and reset
- Create and delete
- Enter and exit
- Start and stop
- Install and uninstall

### Class-Based Context Managers

To create a class-based context manager, add the `.__enter__()` and `.__exit__()` special methods to your class:

| Method | Description |
| --- | --- |
| `.__enter__(self)` | Handles setup logic; called automatically when entering a new context using `with`. Its return value is bound to the `with` target variable. |
| `.__exit__(self, exc_type, exc_value, exc_tb)` | Handles teardown logic; called automatically when leaving the `with` block. If an exception occurs, `exc_type`, `exc_value`, and `exc_tb` hold the exception type, value, and traceback. |

Demo:

```python
>>> class HelloContextManager:
...     def __enter__(self):
...         print("Entering the context...")
...         return "Hello, World!"
...
...     def __exit__(self, exc_type, exc_value, exc_tb):
...         print("Leaving the context...")
...         print(f"{exc_type  = }")
...         print(f"{exc_value = }")
...         print(f"{exc_tb    = }")
...
>>> with HelloContextManager() as hello:
...     print(hello)
...
Entering the context...
Hello, World!
Leaving the context...
exc_type  = None
exc_value = None
exc_tb    = None
```

If an exception occurs during execution of the `with` block, the arguments to `.__exit__()` are set to the exception type, value, and traceback object.

### Handling Exceptions Within Context Managers

If `.__exit__()` returns `True`, then any exception that occurs in the `with` block is swallowed and execution continues at the next statement after `with`. If `.__exit__()` returns `False` (or `None`, the default), exceptions are propagated out of the context.

```python
>>> class HelloContextManager:
...     def __enter__(self):
...         print("Entering the context...")
...         return "Hello, World!"
...
...     def __exit__(self, exc_type, exc_value, exc_tb):
...         print("Leaving the context...")
...         if isinstance(exc_value, IndexError):
...             print(f"An exception occurred in your with block: {exc_type}")
...             print(f"Exception message: {exc_value}")
...             return True
...

>>> with HelloContextManager() as hello:
...     print(hello)
...     hello[100]
...
Entering the context...
Hello, World!
Leaving the context...
An exception occurred in your with block: <class 'IndexError'>
Exception message: string index out of range
```

### Opening Files for Writing

A class-based context manager that opens files for writing directly:

```python
>>> class WritableFile:
...     def __init__(self, file_path):
...         self.file_path = file_path
...
...     def __enter__(self):
...         self.file_obj = open(self.file_path, mode="w")
...         return self.file_obj
...
...     def __exit__(self, *_):
...         if self.file_obj:
...             self.file_obj.close()
...
```

### Redirecting the Standard Output to a File

Sometimes you don't have a useful object to return from `.__enter__()`. In those cases, you can explicitly return `None`, or rely on Python's implicit return value, which is also `None`:

```python
>>> import sys

>>> class StandardOutputRedirector:
...     def __init__(self, new_output):
...         self.new_output = new_output
...
...     def __enter__(self):
...         self.std_output = sys.stdout
...         sys.stdout = self.new_output
...
...     def __exit__(self, *_):
...         sys.stdout = self.std_output
...
```

If you're only redirecting the output of `print()`, you can get the same functionality without a context manager by providing a `file` argument to `print()`:

```python
>>> with open("hello.txt", "w") as file:
...     print("Hello, World!", file=file)
...
```

### Measuring Execution Time

A stateful context manager to measure execution time:

```python
>>> from time import perf_counter, sleep
>>> class Timer:
...     def __enter__(self):
...         self.start = perf_counter()
...
...     def __exit__(self, *_):
...         end = perf_counter()
...         print(f"Elapsed time: {end - self.start:.4f} seconds")
...

>>> with Timer():
...     sleep(0.5)
...
Elapsed time: 0.5051 seconds
```

### Indenting Text

A context manager that manages text indentation level:

```python
class Indenter:
    def __init__(self, width=2):
        self.indentation = " " * width
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *_):
        self.level -= 1

    def print(self, text):
        print(self.indentation * self.level + text)
```

Returning `self` from `.__enter__()` allows you to reuse the same context manager across several nested `with` statements, changing the text indentation level every time you enter and exit a given context.

### Function-Based Context Managers

Python's `contextlib.contextmanager` decorator provides an alternative way to implement the context management protocol. Decorate an appropriately coded generator function with `@contextmanager` to get a function-based context manager:

```python
>>> from contextlib import contextmanager

>>> @contextmanager
... def hello_context_manager():
...     print("Entering the context...")
...     yield "Hello, World!"
...     print("Leaving the context...")
...

>>> with hello_context_manager() as hello:
...     print(hello)
...
Entering the context...
Hello, World!
Leaving the context...
```

Before the `yield` statement is the setup section; after it is the teardown section. The `yield` statement optionally provides the object assigned to the `with` target variable.

The `@contextmanager` decorator reduces boilerplate: instead of writing a whole class with `.__enter__()` and `.__exit__()`, implement a generator function with a single `yield`.

Realistic example reimplementing `WritableFile`:

```python
>>> from contextlib import contextmanager

>>> @contextmanager
... def writable_file(file_path):
...     try:
...         file = open(file_path, mode="w")
...         yield file
...     finally:
...         file.close()
...

>>> with writable_file("hello.txt") as file:
...     file.write("Hello, World!")
...
13
```

### Creating an Asynchronous Context Manager

To create an asynchronous context manager, define `.__aenter__()` and `.__aexit__()`:

```python
import asyncio
import aiohttp

class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()
```

A common practice is to implement all four special methods (`__aenter__`, `__aexit__`, `__enter__`, `__exit__`) so your context manager works with both `with` and `async with`.

## Conclusion

The `with` statement is an essential tool for Python developers. It facilitates resource management and ensures that resources are properly released, even in the presence of exceptions.

In this tutorial, you've learned how to:

- Use Python's `with` statement for resource management
- Understand the context manager protocol
- Create custom class-based and function-based context managers
- Work with asynchronous context managers for concurrent tasks

## See Also

- [Reading and Writing Files in Python](reading-writing-files.md)
- [Vault Security](../data-archivist/vault-security.md)
- [Data Archivist Project Overview](../data-archivist/data-archivist-overview.md)
