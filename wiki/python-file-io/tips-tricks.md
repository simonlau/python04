# Tips and Tricks

> Sources: Real Python, James Mertz, 2019-02-20
> Raw: [2026-10-30-reading-and-writing-files-in-python](../../raw/python-file-io/2026-10-30-reading-and-writing-files-in-python.md)
> Updated: 2026-10-30

## Overview

Additional techniques to grow your file-handling skills beyond the basics.

## `__file__`

The `__file__` attribute is a special attribute of modules, similar to `__name__`. It is “the pathname of the file from which the module was loaded, if it was loaded from a file.” `__file__` returns the path relative to where the initial Python script was called. For the full system path, use `os.getcwd()`.

## Appending to a File

To append to a file or start writing at the end of an already populated file, use the `'a'` character for the `mode` argument:

```python
with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')
```

The beginning of the file stays unchanged and `Beagle` is added to the end.

## Working With Two Files at the Same Time

You can read a file and write to another file at the same time:

```python
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
```

## Creating Your Own Context Manager

For finer control of the file object, place it inside a custom class and add `__enter__` and `__exit__` magic methods to create a context manager:

```python
class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()
```

Use it similarly to the `open()` built-in:

```python
with my_file_reader('dog_breeds.txt') as reader:
    # Perform custom class operations
    pass
```

## See Also

- [Reading and Writing Files in Python](reading-writing-files.md)
- [Vault Security](../data-archivist/vault-security.md)
