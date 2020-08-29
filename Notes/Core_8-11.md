# [8] Exceptions

### [8] Overview

Key Concepts

1. Raising an exception interrupts flow
2. Handling an exception to allow control flow to be transferred to exception handler
3. Unhandled exceptions
4. Exception objects is transferred from raised exception to handler

### [8] Exceptions and Control Flow

See `exceptional.py`

### [8] Handling Exceptions

See `exceptional.py`

### [8] Exceptions and Programmer Errors

See `exceptional.py`

Programmer errors include:

- IndentationError
- SyntaxError
- NameError

And should almost NEVER be caught

`pass` keyword is a no-oop for empty blocks that give `IndentationError`s

Exceptions can not be ignored

- Error codes are easy to ignore by the caller
- Checks are always required

`raise` re-raises the exception that is currently being handled

### [8] Exceptions Are Part of the API

see `roots.py`

Use standard Exception Types

Standard Types

- Python provides standard exceptions types for signalling common errors

Invalid argument values

- Use `ValueError` for arguments of the right type but with an invalid value

Exception constructors

- Use raise `ValueError()` to raise a new `ValueError`

### [8] Exceptions and Protocols

Exceptions are as much a part of the functions specification as the arguments it excepts
Existing built-in exceptions are often the right ones to use
Sequences should raise `IndexError` for out of bounds
Follow existing patterns

Common Exception Types

- `IndexError` => An integer index is out of range
- `ValueError` => An object is of the correct type but has an inappropriate value
  - ex: `int("jim")`
- `KeyError` => When a lookup in a mapping fails

### [8] Avoid explicit type checks

Avoid catching `TypeError`

- Increase function reusability
- Let TypeErrors arise on their own

## [8] Ask forgiveness...

Best to attempt operations and then "ask for forgiveness" by handling errors than interspersing error handling throughout your code
`EAFP`
Exceptions can be handled non-locally

EAFP plus Exceptions

1. Exceptions are not easily ignored
2. Error codes are silent by default
3. Exceptions plus EAFP **makes it hard for problems to be silently ignored**

### [8] Cleanup Actions

```
try:
    # try-block
finally:
    # executed no matter how the try-block terminates
```

Example of Cleaning up from Exceptions:

```
import os
import sys

def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    finally:
        os.chdir(original_path)
```

- restores original working directory under all circumstances
- code in the finally block executes whether exception leavews the try block normally by reaching the end of the block, or exceptionally by an exception being raised
  - You can then combine with except blocks to handle the errors

```
import os
import sys

def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)
```

- Errors should never pass silently, unless explicitly silenced

### [8] Platform-Specific Code

- OS-specific modules
- Windows: msvcrt
- Unix: tty, termios, and sys modules

Example of error being ignored explicitly

- If not Windows machine, except `ImportError` and run Unix block

```
"""keypress - A module for detecting a single keypress."""
try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a single character string"""
        return msvcrt.getch()

except ImportError:
    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character string"""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return c


    # if either of the Unix=-specific tty or termios are not found,
    # we allow the ImportError to propagate from here
```

- The caller can take _alternative actions_ if both imports fail.
  - ex: They could _downgrade_ to using input().
-

# [9] Iteration and Iterables

### [9] List and Set Comprehensions

`Comprehensions` => Concise syntax for describing lists, sets, and dictionaries in a declarative or functional style

ex:

```
words = "The quick brown fox jumped over the lazy dog".split()
[len(word) for word in words]
=> [3, 5, 5, 3, 6, 4, 3]... etc.
```

List Comprehension Syntax
`[expr(item) for item in iterable]`

Equivalent Context

```
lengths = []
for word in words:
  lengths.append(len(word))
```

Set Comprehensions

```
from math import factorial
s = {len(str(factorial(x))) for x in range(20)}
print(s)
{1, 2, 3, 4, 5, 6, 7}...
```

### [9] Dictionary Comprehensions

Dict Comprehensions

```
{
  key_expr(item): value_expr(item)
  for item in iterable
}
```

ex1:

```
country_to_capital = { 'United Kingdom': 'London', 'Brazil': 'Brasilia' }
capital_to_country = { capital: country for country, capital in country_to_capital.items()}
// inverst ditionary
```

ex2:

```
words = ["hi", "hello", "foxtrot", "hotel"]
{ x[0]: x for x in words }
{ h: 'hotel', 'f': 'foxtrot' }
```

Comprehension expressions can be arbitrarily complex, but avoid over-excessive complexity for the sake of readability

### [9] Filtering Comprehensions

ex: `[x for x in range(101) if is_prime(x)]`

### [9] Iteration Protocols

iterable objects vs iterator objects

iterable "protocol"

- Can be passed to iter() to produce an iterator

Iterator objects

- Support the iterator protocol
- Can be passed to next() to get the next value in the sequence

ex:

```
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
next(iterator)
'Spring'
next(iterator)
'Summer'
next(iterator)
'Autumn'
next(iterator)
'Winter'
next(iterator)

=> raises exception of `StopIteration`
```
