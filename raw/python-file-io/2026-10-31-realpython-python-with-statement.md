# Python's with Statement: Manage External Resources Safely

> Source: https://realpython.com/python-with-statement/
> Collected: 2026-10-31
> Published: 2026-10-25

## Overview

Python's `with` statement allows you to manage external resources safely by using objects that support the context manager protocol. These objects automatically handle the setup and teardown phases of common operations.

By using the `with` statement alongside appropriate context managers, you can focus on your core logic while the context managers prevent resource leaks like unclosed files, unreleased memory, or dangling network connections.

By the end of this tutorial, you'll understand that:

- Python's `with` statement automates the process of setting up and tearing down computational resources using context managers.
- Using `with` reduces code complexity and prevents resource leaks by ensuring proper resource release, even if exceptions occur.
- A context manager in Python is an object that implements `.__enter__()` and `.__exit__()` methods to manage resources safely.

## Managing External Resources in Python

Properly managing external resources, such as files, locks, and network connections, is a common requirement in programming. Sometimes, a program uses a given resource and doesn't release the associated memory when it no longer needs the resource. This kind of issue is called a memory leak because the available memory shrinks every time you create a new instance of a resource without releasing the unneeded ones.

Managing resources properly is often a tricky task. It requires setup and teardown phases. The latter phase requires you to perform cleanup actions, like closing a file, releasing a lock, or closing a network connection. If you forget to perform these cleanup actions, then your application keeps the resource occupied. This behavior might compromise valuable system resources, such as memory and network bandwidth.

For example, writing text to files is usually a buffered operation. This means that calling `.write()` on a file won't immediately result in writing text to the physical file, but to a temporary buffer. Sometimes, when the buffer isn't full, developers forget to call `.close()` and part of the data can be lost.

Another possibility is that your application runs into errors or exceptions that cause the control flow to bypass the code responsible for releasing the resource at hand.

Here's an example where you use the built-in `open()` function to write some text to a file:

```python
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()
```

This code doesn't guarantee the file will be closed if an exception occurs during the call to `.write()`. In this situation, the code might never call `.close()`, and your program will leak a file descriptor. Failing to release a file descriptor on some operating systems can prevent other programs from accessing the underlying file.

In Python, you can use a couple of general approaches to deal with resource management:

1. A `try ... finally` construct
2. A `with` construct

The first approach is quite generic and allows you to provide setup and teardown code to manage any kind of resource. However, it's a little bit verbose, and you might forget some cleanup actions if you use this construct in several places.

The second approach provides a straightforward way to provide and reuse setup and teardown code. In this case, you'll have the limitation that the `with` statement only works with context managers.

### The `try ... finally` Construct

Working with files is probably the most common example of resource management in programming. In Python, you can use a `try ... finally` construct to handle opening and closing files properly:

```python
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
finally:
    file.close()
```

In this example, you open the `hello.txt` file using `open()`. To write some text into the file, you wrap the call to `.write()` in a `try` statement with a `finally` clause. This clause guarantees that the file is properly closed by calling `.close()`, even if an exception occurs during the call to `.write()` in the `try` clause. Remember that the `finally` clause always runs.

The `try` block can potentially raise exceptions. You can handle these exceptions with an `except` clause:

```python
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()
```

Even though the `try ... finally` construct works correctly, Python has a more compact and elegant solution: the `with` statement.

### The `with` Statement

The Python `with` statement creates a runtime context that allows you to execute a code block under the control of a context manager. PEP 343 added the `with` statement to make it possible to factor out common use cases of the `try ... finally` construct.

Compared to the traditional `try ... finally` construct, the `with` statement makes your code clearer, safer, and more readable. Many classes and objects in the standard library support the `with` statement by implementing the context manager protocol. For example, when you call `open()`, you get a file object that supports this protocol and, therefore, the `with` statement.

To write a `with` statement, you need to use the following general syntax:

```python
with expression [as obj]:
    <block>
```

The context manager object results from evaluating the `expression` after the `with` keyword. In other words, `expression` must return an object that implements the context management protocol. This protocol consists of two special methods:

1. `.__enter__()` is called by the `with` statement to enter the runtime context.
2. `.__exit__()` is called when the execution leaves the `with` code block.

The `as` specifier is optional. If you provide an `obj` variable with `as`, then the return value of calling `.__enter__()` on the context manager object is bound to that variable.

Note: Some context managers return `None` from `.__enter__()` because they have no useful object to give back to the caller. In these situations, specifying an `obj` variable makes no sense.

Here's how the `with` statement works internally:

1. Execute `expression` to obtain a context manager object.
2. Call `.__enter__()` on the context manager and bind its return value to `obj` if provided.
3. Execute the `with` code block.
4. Call `.__exit__()` on the context manager when the `with` code block finishes.

The `.__enter__()` method typically provides the setup logic. The `with` statement is a compound statement that starts a code block, like other compound statements, such as conditional statements and `for` loops.

Inside this code block, you can run one or more statements. Typically, you use the `with` code block to manipulate `obj` if applicable.

Once the `with` code block finishes, Python automatically calls `.__exit__()`. This method typically provides the teardown logic or cleanup code, such as calling `.close()` on an open file object. That's why the `with` statement is so useful. It makes properly acquiring and releasing resources a breeze.

Here's how to open your `hello.txt` file for writing using the `with` statement:

```python
with open("hello.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World!")
```

When you run this `with` statement, `open()` returns an `io.TextIOBase` object. This object supports the context manager protocol, so the `with` statement calls `.__enter__()` and assigns its return value to `file`. Then, you can manipulate the file inside the `with` code block. When the block ends, Python automatically calls `.__exit__()`, which closes the file for you, even if an exception occurs in the `with` code block.

This `with` construct is shorter than its `try ... finally` equivalent construct, but it's also less generic because you can only use the `with` statement with objects that support the context management protocol. In contrast, `try ... finally` allows you to perform cleanup actions for any object, even if it doesn't implement the context management protocol.

The `with` statement also supports multiple context managers. You can supply any number of context managers separated by commas:

```python
with A() as a, B() as b:
    <block>
```

This works like nested `with` statements, but without nesting. It might be useful when you need to open two files at a time—the first for reading and the second for writing:

```python
with open("hello.txt") as in_file, open("output.txt", "w") as out_file:
    for line in in_file:
        out_file.write(line.upper())
```

In this example, you read and transform the content of `hello.txt` line by line. Then, you write each processed line to `output.txt` within the same code block.

The `with` statement can make the code that deals with system resources more readable, concise, and safer. It helps avoid resource leaks by making it almost impossible to forget to clean up, close, and release resources after you're done with them.

Using `with` allows you to abstract away most of the resource handling logic. Instead of using explicit `try ... finally` constructs with setup and teardown logic, you can pack this logic into a context manager and handle it using the `with` statement to avoid repetition.

## Using Python's `with` Statement

The `with` statement is useful in several common situations. Several objects in Python's standard library provide support for the context manager protocol, so you can use them in `with` statements for multiple tasks that imply setup and teardown logic.

### Working With Files

So far, you've used `open()` to manipulate files in a `with` construct. Managing files this way is generally recommended because it ensures that opened file descriptors are automatically closed after the flow of execution leaves the `with` code block.

Again, a common way to open a file in a `with` statement is through the `open()` function:

```python
with open("hello.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World!")
```

In this example, the context manager closes the file after leaving the `with` code block. A common mistake you might encounter is shown below:

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

The first `with` successfully writes `"Hello, World!"` into `hello.txt`. Note that `.write()` returns the number of bytes written into the file—13 bytes in this example. When you try to run a second `with`, you get a `ValueError` because the file is already closed.

Another way to use the `with` statement to open and manage files is by using the `.open()` method on a `Path` object:

```python
>>> import pathlib
>>> file_path = pathlib.Path("hello.txt")
>>> with file_path.open("w", encoding="utf-8") as file:
...     file.write("Hello, World!")
...
13
```

`Path` is a class that represents concrete paths to physical files on your computer. Calling `.open()` on a `Path` object that points to a physical file opens it just like `open()` would. So, `Path.open()` works similarly to `open()`, but the file path is automatically provided by the `Path` object you call the method on.

The `pathlib` package provides an elegant, straightforward, and Pythonic way to manipulate file system paths. You should consider using `Path.open()` in your `with` statements as a best practice in Python.

Finally, whenever you load an external file, your program should check for possible issues, such as a missing file, writing and reading access, and so on. Here's a pattern that you should consider using when working with files:

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

In this example, you wrap the `with` statement in a `try ... except` block. If an `OSError` occurs during the execution of `with`, then you use the `logging` module to log the error with a user-friendly and descriptive message.

### Traversing Directories

The `os` module provides a function called `scandir()` that returns an iterator over `os.DirEntry` objects corresponding to the entries in a given directory. This function is specially designed to provide optimal performance when you're traversing a directory structure.

A call to `scandir()` with a directory path as an argument returns an iterator that supports the context management protocol:

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

In this example, you write a `with` statement with `os.scandir()` as the context manager supplier. Then, you iterate over the entries in the working directory represented by `"."` and print their names and sizes on the screen. In this case, `.__exit__()` calls `scandir.close()` to close the iterator and release the acquired resources.

### Performing High-Precision Calculations

The `decimal` module provides a handy way to tweak the precision to use in a given calculation that involves decimal numbers. The precision defaults to 28 places, but you can change it to meet your specific requirements.

A quick way to perform calculations with a custom precision is using `localcontext()` from `decimal`:

```python
>>> from decimal import Decimal, localcontext
>>> with localcontext(prec=42):
...     Decimal("1") / Decimal("42")
...
Decimal('0.0238095238095238095238095238095238095238095')
>>> Decimal("1") / Decimal("42")
Decimal('0.02380952380952380952380952381')
```

Here, `localcontext()` returns a context manager that creates a context allowing you to perform calculations using a custom precision. In the `with` code block, you have a precision of 42 places. When the `with` code block finishes, the precision is back to its default value of 28 places.

### Handling Locks in Multithreaded Programs

The `threading.Lock` class in the Python standard library also supports the `with` statement. This class provides a primitive lock to prevent multiple threads from modifying a shared resource at the same time in a multithreaded application.

You can use a `Lock` object in a `with` statement to automatically acquire and release a given lock:

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

The `with` statement in the second example automatically acquires and releases a lock when the flow of execution enters and leaves the statement. This way, you can focus on what really matters in your code and forget about those repetitive operations.

In this example, the lock in the `with` statement creates a protected region known as the critical section, which prevents concurrent access to the account balance.

### Testing for Exceptions With pytest

Several third-party libraries include objects that also support the context management protocol. Say you're testing your code with pytest. Some of your functions and code blocks raise exceptions under certain situations, and you want to test those cases. To do that, you can use `pytest.raises()`, which allows you to assert that a block of code or a function call raises a specific exception.

The `pytest.raises()` function returns a context manager, so you can use that object in a `with` statement:

```python
>>> import pytest
>>> with pytest.raises(ZeroDivisionError):
...     1 / 0
...
>>> favorites = {"fruit": "apple", "pet": "dog"}
>>> favorites["car"]
Traceback (most recent call last):
    ...
KeyError: 'car'
>>> with pytest.raises(KeyError):
...     favorites["car"]
...
```

You can use all these `pytest.raises()` features to capture the exceptions you raise from your functions and code blocks. For example, if you want to verify the error message, then you can do something like this:

```python
>>> with pytest.raises(ZeroDivisionError) as exc:
...     1 / 0
...
>>> assert str(exc.value) == "division by zero"
```

### Summarizing the `with` Statement's Advantages

To summarize what you've learned so far, here's a non-exhaustive list of the general benefits of using the `with` statement:

- Makes resource management safer than using equivalent `try ... finally` constructs
- Encapsulates standard uses of `try ... finally` constructs in context managers
- Allows using context managers to pack the code that handles setup and teardown logic
- Helps prevent resource leaks

Using the `with` statement consistently can improve the general quality of your code and make it safer by preventing resource leak problems.

## Using the `async with` Statement

The `with` statement also has an asynchronous version, `async with`. You can use it to write context managers that work within asynchronous code. It's quite common to see `async with` in that kind of code, as many I/O-bound tasks involve setup and teardown phases.

For example, say you need to code an asynchronous function to check whether some websites are online. To do that, you can use `aiohttp` and `asyncio`. Note that `aiohttp` is a third-party package that you need to install by running `python -m pip install aiohttp==3.14.5` on your command line.

Here's a quick script that implements the required functionality:

```python
import asyncio
import aiohttp

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

asyncio.run(main())
```

The `async with` statement works like a regular `with` statement, but it requires an asynchronous context manager. In other words, it needs a context manager that's able to suspend execution in its enter and exit methods.

Asynchronous context managers implement the special methods `.__aenter__()` and `.__aexit__()`, which are the asynchronous counterparts to `.__enter__()` and `.__exit__()` in regular context managers.

When you use the `async with ctx_mgr` construct, Python implicitly calls `await ctx_mgr.__aenter__()` on entry and `await ctx_mgr.__aexit__()` on exit. This allows asynchronous context management to work seamlessly.

## Creating Custom Context Managers

You've already worked with context managers from the standard library and third-party libraries. There's nothing special or magical about `open()`, `threading.Lock`, `decimal.localcontext()`, and the others. They simply return objects that implement the context management protocol.

You can provide the same functionality by implementing the `.__enter__()` and `.__exit__()` special methods in your class-based context managers. You can also create custom function-based context managers using the `contextlib.contextmanager` decorator from the standard library and an appropriately coded generator function.

In practice, context managers and the `with` statement aren't limited to resource management. They allow you to provide and reuse common setup and teardown code. In other words, you can use a context manager to handle any pair of operations that must occur before and after a task or procedure, such as:

- Open and close
- Lock and release
- Change and reset
- Create and delete
- Enter and exit
- Start and stop
- Install and uninstall

You can provide code to safely manage any of these pairs of operations in a context manager. Then, you can reuse that context manager in `with` statements throughout your code. This helps prevent errors, reduces repetitive boilerplate code, and makes your APIs safer, cleaner, and more user-friendly.

### Coding Class-Based Context Managers

To create a class-based context manager, you need to add the `.__enter__()` and `.__exit__()` special methods to your class:

| Method | Description |
| --- | --- |
| `.__enter__(self)` | This method handles the setup logic and is called automatically when entering a new context using the `with` statement. Its return value is bound to the `with` target variable. |
| `.__exit__(self, exc_type, exc_value, exc_tb)` | This method handles the teardown logic and is automatically called when the flow of execution leaves the `with` block. If an exception occurs, then `exc_type`, `exc_value`, and `exc_tb` hold the exception type, value, and traceback information, respectively. |

Next, you'll learn more about writing your own context manager and dive a bit deeper into the implementation of these special methods.

#### Writing a Demo Class-Based Context Manager

When the `with` statement executes, Python calls `.__enter__()` on the context manager object to set up the new runtime context. If you provide a target variable with the `as` specifier, then the return value of `.__enter__()` is assigned to that variable. When the flow of execution leaves the context, `.__exit__()` is called.

Below is a demo class-based context manager that shows how Python calls the `.__enter__()` and `.__exit__()` methods in a `with` construct:

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

In `.__enter__()`, you print a message to indicate that the flow of execution is entering a new context. Then, you return the `"Hello, World!"` string. In `.__exit__()`, you print a message to signal that the execution flow is leaving the context. You also print the content of the three arguments.

When the `with` statement runs, Python creates a new instance of `HelloContextManager` and calls its `.__enter__()` method. Next, Python runs the `with` code block, which prints `hello` to the screen. Note that `hello` holds the return value of `.__enter__()`, which is `"Hello, World!"` in this example.

When the execution flow exits the `with` code block, Python calls `.__exit__()`. If no exception occurs in the `with` code block, then the three arguments to `.__exit__()` are set to `None`.

Now, what if an exception occurs during the execution of the `with` block?

```python
>>> with HelloContextManager() as hello:
...     print(hello)
...     hello[100]
...
Entering the context...
Hello, World!
Leaving the context...
exc_type  = <class 'IndexError'>
exc_value = IndexError('string index out of range')
exc_tb    = <traceback object at 0x7f0cebcdd080>
Traceback (most recent call last):
  ...
IndexError: string index out of range
```

In this example, you try to retrieve the value at index `100` in the string `"Hello, World!"`. This action raises an `IndexError` exception because the string doesn't have 100 characters. Therefore, the arguments to `.__exit__()` are set as follows:

- `exc_type`: the exception class, `IndexError`.
- `exc_value`: the concrete exception object with a descriptive message.
- `exc_tb`: the traceback object.

#### Handling Exceptions Within Context Managers

If the `.__exit__()` method returns `True`, then any exception that occurs in the `with` block is swallowed and the execution continues at the next statement after `with`. If `.__exit__()` returns `False`, then exceptions are propagated out of the context. This is also the default behavior when the method doesn't return anything explicitly.

You can take advantage of these behaviors to encapsulate exception handling inside the context manager or to propagate the exceptions as needed.

As an example of encapsulating exception handling in a context manager:

```python
>>> class HelloContextManager:
...     def __enter__(self):
...         print("Entering the context...")
...         return "Hello, World!"
...
...     def __exit__(self, exc_type, exc_value, exc_tb):
...         print("Leaving the context...")
...         if isinstance(exc_value, IndexError):
...             # Handle IndexError here...
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

In `.__exit__()`, you check if `exc_value` is an instance of `IndexError` using the built-in `isinstance()` function. If so, you print a couple of informative messages and finally return with `True`.

Again, returning a `True` makes it possible to swallow the exception and continue the normal execution after the `with` code block.

#### Opening Files for Writing

Now that you know how to implement the context management protocol, you can code a more realistic example. For instance, below is how you can create a context manager that opens files for writing directly:

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

`WritableFile` allows you to open the file for writing using the `"w"` mode of `open()`. You do this in the `.__enter__()` method. In the `.__exit__()` method, you close the file to release the acquired resources. Note how you use the `*args` syntax to maintain compatibility with the context management protocol. Since you don't need these arguments, you use a single underscore to suppress a potential linter warning about unused variables.

Here's how you can use your context manager:

```python
>>> with WritableFile("hello.txt") as file:
...    file.write("Hello, World!")
...
13
```

After running this code, you'll have a `hello.txt` file containing the `"Hello, World!"` string.

#### Redirecting the Standard Output to a File

A subtle detail to consider when you're implementing the context manager protocol is that sometimes you don't have a useful object to return from `.__enter__()`—and therefore nothing meaningful to assign to the target variable in the `with` header. In those cases, you can explicitly return `None`, or just rely on Python's implicit return value, which is also `None`.

For example, say you need to temporarily redirect the standard output, `sys.stdout`, to a given file on your disk. To do this, you can create a context manager like the following:

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

This context manager takes a file object as an argument. In `.__enter__()`, you reassign the standard output, `sys.stdout`, to an instance attribute to avoid losing the reference to it. Then, you reassign the standard output to point to the file on your disk. In `.__exit__()`, you restore the standard output to its original value.

To use `StandardOutputRedirector`, you can do something like this:

```python
>>> with open("hello.txt", "w") as file:
...     with StandardOutputRedirector(file):
...         print("Hello, World!")
...     print("Back to the standard output...")
...
Back to the standard output...
```

The outer `with` statement provides the file object that you'll use as your new output, `hello.txt`. The inner `with` temporarily redirects the standard output to `hello.txt`, so the first call to `print()` writes directly to that file instead of printing `"Hello, World!"` to your screen. When you leave the inner `with` code block, the standard output is set back to its original value.

Note: If you're only redirecting the output of `print()`, then you can get the same functionality without a context manager. You just need to provide a `file` argument to `print()` as shown below:

```python
>>> with open("hello.txt", "w") as file:
...     print("Hello, World!", file=file)
...
```

#### Measuring Execution Time

Just like any other class, a context manager can encapsulate some internal state. The following example shows how to create a stateful context manager to measure the execution time of a given piece of code:

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
...     # The code to measure goes here...
...     sleep(0.5)
...
Elapsed time: 0.5051 seconds
```

In the `.__enter__()` method, you call `time.perf_counter()` to get the current timestamp at the beginning of a `with` code block and store it in the `.start` attribute. This value represents the context manager's initial state.

Once the `with` block ends, `.__exit__()` gets called. The method gets the time at the end of the block and stores the value in a local variable `end`. Finally, it prints a message to inform you of the elapsed time.

#### Indenting Text

What if the resource you wanted to manage is the text indentation level in some kind of report generator application? For example, say that you want to write code that generates HTML output like the following:

```html
<div>
  <p>
    Hello, World!
  </p>
</div>
```

Here's how you can implement this functionality using a class-based context manager:

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

Here, `.__enter__()` increments `.level` by `1` every time the flow of execution enters the context. The method also returns the current instance, `self`. In `.__exit__()`, you decrease `.level`, so the printed text steps back one indentation level each time you exit the context.

The key point here is that returning `self` from `.__enter__()` allows you to reuse the same context manager across several nested `with` statements. This changes the text indentation level every time you enter and exit a given context.

### Creating Function-Based Context Managers

Python's `contextlib.contextmanager` decorator provides an alternative and convenient way to implement the context management protocol. If you decorate an appropriately coded generator function with `@contextmanager`, then you get a function-based context manager that automatically provides both `.__enter__()` and `.__exit__()`.

The pattern to create a context manager using `@contextmanager` along with a generator function goes like this:

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

In this example, you can identify two visible sections in `hello_context_manager()`. Before the `yield` statement, you have the setup section. There, you can place the code that acquires the needed resources. Everything before the `yield` runs when the flow of execution enters the context.

After the `yield` statement, you have the teardown section where you can release resources and do the cleanup. The code after `yield` runs at the end of the `with` block. The `yield` statement itself optionally provides the object that will be assigned to the `with` target variable, if any.

This implementation and the one that uses the context management protocol are equivalent. Depending on which one you find suitable for your current problem, you might choose one over the other. A downside of the function-based implementation is that it requires an understanding of advanced Python topics, such as decorators and generators.

The `@contextmanager` decorator reduces the boilerplate required to create a context manager. Instead of writing a whole class with `.__enter__()` and `.__exit__()` methods, you just need to implement a generator function with a single `yield` that produces whatever you want `.__enter__()` to return.

For a more realistic example, you can use the `@contextmanager` to reimplement your `WritableFile` context manager. Here's what rewriting it with this technique will look like:

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

In this case, `writable_file()` is a generator function that opens a file for writing. Then, it temporarily suspends its execution and yields the file so that `with` can bind it to its target variable. When the execution flow leaves the `with` code block, the function continues to execute and closes the file correctly.

### Creating an Asynchronous Context Manager

To create an asynchronous context manager, you need to define the `.__aenter__()` and `.__aexit__()` methods. The script below is a reimplementation of the example about checking whether a website is online:

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

async def check(url):
    async with AsyncSession(url) as response:
        print(f"{url}: status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

asyncio.run(main())
```

This script works like the previous implementation. The main difference is that, in this example, you extract the logic of the original outer `async with` statement and encapsulate it in `AsyncSession`.

In `.__aenter__()`, you create an `aiohttp.ClientSession()`, await the `.get()` response, and finally return the response itself. In `.__aexit__()`, you close the session, which corresponds to the teardown logic in this specific case. Note that `.__aenter__()` and `.__aexit__()` must return awaitable objects, so you need to define them using the `async def` keywords.

Finally, a common practice when you're writing asynchronous context managers is to implement the four special methods:

1. `.__aenter__()`
2. `.__aexit__()`
3. `.__enter__()`
4. `.__exit__()`

Doing so makes your context manager usable with both `with` and `async with` statements.

## Conclusion

You've learned about Python's `with` statement, which helps you manage external resources safely. You've also learned how context managers can automatically handle the setup and teardown phases of working with external resources, and how these tools can prevent resource leaks and improve code safety.

Additionally, you learned how to create custom context managers using both class-based and function-based approaches, and even how to implement asynchronous context managers for concurrent programming.

The `with` statement is an essential tool for Python developers. It facilitates resource management and ensures that resources are properly released, even in the presence of exceptions.

In this tutorial, you've learned how to:

- Use Python's `with` statement for resource management
- Understand the context manager protocol
- Create custom class-based and function-based context managers
- Work with asynchronous context managers for concurrent tasks

With these skills, you can write more reliable and safer Python code by managing resources correctly and avoiding potential leaks. This knowledge strengthens your ability to build robust, maintainable applications.

## Frequently Asked Questions

**What is the `with` statement in Python?**

You use Python's `with` statement to manage resource setup and teardown automatically, ensuring resources are properly released after use, even if exceptions occur.

**What is the advantage of using `with`?**

The `with` statement reduces code complexity, enhances readability, and—more importantly—prevents resource leaks by ensuring resources are released correctly after use.

**What is a context manager?**

A context manager is a Python object that implements the `.__enter__()` and `.__exit__()` special methods to safely manage resources by automating setup and teardown steps.
