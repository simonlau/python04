# How to print to stderr and stdout in Python?

> Source: https://www.geeksforgeeks.org/python/how-to-print-to-stderr-and-stdout-in-python/
> Collected: 2026-10-31
> Published: 2025-07-12

## Overview

In Python, whenever we use `print()` the text is written to Python's **sys.stdout**, whenever `input()` is used, it comes from **sys.stdin**, and whenever exceptions occur it is written to **sys.stderr**.

We can redirect the output of our code to a file other than stdout. The reason can be to keep a log of your code's output or to make your code shut up i.e. not sending any output to the stdout.

## What is Python stderr?

This file handle receives error information from the user program. The Standard error returns errors stderr. It is comparable to stdout in that it likewise prints straight to the console, but the key distinction is that it prints only Exceptions and Error messages which is why it is called Standard Error in Python.

### Method 1: Using Python stderr

```python
import sys

def print_to_stderr(*a):

    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stderr)


print_to_stderr("Hello World")
```

### Method 2: Using Python sys.stderr.write() function

When used in interactive mode, `sys.stderr.write()` accomplishes the same task as the object it stands for, with the exception that it also prints the text's letter count.

```python
import sys

print("Example 1")
print("Example 2", file=sys.stderr)
sys.stderr.write("Example 3")
```

### Method 3: Using Python logging.warning function

A built-in Python package tool called `logging.warning` enables publishing status messages to files or other output streams. The file may provide details about which portion of the code is run and any issues that have come up.

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

## What is Python stdout?

This file handle receives regular information from the user program. The output is made available through the standard output stdout from sys module.

### Method 1: Using Python sys.stdout method

stdout in Python is similar to sys.stdin, but it directly displays anything written to it to the Console.

```python
import sys

def print_to_stdout(*a):

    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stdout)

print_to_stdout("Hello World")
```

### Method 2: Using Python print() function

Python `print()` function prints the message to the screen or any other standard output device. In the `print()` function, it requires an empty parenthesis at the end that tells Python to execute the function rather than calling it by name.

```python
print( "Hello GeeksforGeeks" )
```

Output:

```
Hello GeeksforGeeks
```

### Method 3: Using Python sys.stdout.write() function

`sys.stdout.write()` serves the same purpose as the object stands for except it prints the number of letters within the text too when used in interactive mode.

```python
import sys

a = 11

print(a)
print(a, file=sys.stdout)
sys.stdout.write(a)
```
