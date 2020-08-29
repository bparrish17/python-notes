# [2] Installing and Starting Python

### [2] The Python Standard Library

Importing Modules:

`import math`

> math.factorial(5) // 120

`from math import factorial`

> factorial(5) // 120

`from math import factorial as fac`

> fac(5) // 120

`from math import (factorial, exp, sqrt)`

`from words import *` - not recommended

Math Operators
"/" => float division
"//" => integer division

In many other programming languages, regular signed integers can store values smaller than 2^31, so 12!

- However, Python is limited to the memory in your computer

# [3] Scalar Types, Operators, and Control Flow

### [3] Overview

Booleans

"None" => null
bool(0) => False
bool(0.0) => False
bool(1.0) => True
bool([]) => False
bool([1]) => True
bool('') => False
bool('Hello') => True

### [3] Relational Operators

Equivalence

"is" => InstanceOf
e.g.
x = None
x is None => True

== equality
!= inequality

[3] Control Flow

if statement ex:

```
if expression:
    block

```

if/else statement ex:

```
if expression:
  block
else
  block

```

if/else if statement ex:

```
if expression:
  block
elif expressionB:
  block
```

### [3] While Loops

can "break" from loop, e.g.

```
while <condition>:
  response = input()
  if int(response) % 7 == 0:
    break

```

# [4] Strings, Collections, and Iteration

### [4] String

`str` keyword
immutable!

multiline strings
"""this
is a multiline
string""" (or ''')
=> 'this\nis a multiline\nstring'

### [4] String Literals

to create a "raw" string, prefix with lowercase r
e.g.

```
path = r'C:\users\brianparrish\Documents'

s = 'parrot'
s[4] = 'o'
```

capitalization:

```
c = 'barcelona'
c.capitalize() => 'Barcelona' // creates a VERSION of the original string, does not mutate `c`
```

### [4] Bytes

prefix string with `b`
e.g. `b'data'`

bytes are "encoded" strings and strings are "decoded" bytes

- e.g. utf8 encoding

### [4] Lists

Sequences of objects
Mutable
e.g. `[1, 9, 8]`

```
a = ['apple', 'orange', 'pear']
a[1] = 'grape'

=> ['apple', 'grape', 'pear']


b = []
b.append('hello')

=> ['hello']

list('word')
=> ['w', 'o', 'r', 'd']
```

### [4] Dict

maps keys to values
basically an object
also mutable

```
dct = { 'a': 1 }
dct['a'] = 2

=> { 'a': 2 }
```

### [4] For-Loops

```
for item in iterable:
  block
```

# [5] Modularity

### [5] **name**

Specially named variable that helps us detect whether a module is run as a script or imported into another module

e.g... importing sandbox.py into Python REPL

File: `sandbox.py`

```
print(__name__)
```

REPL:

```
import sandbox
> sandbox
```

e.g... running as script from CLI
`python sandbox.py`

> `__main__`

This way you can check inside the module itself to see if it was being imported. If it's being imported, you don't run it but if you run it as a script you go ahead and run it...

in file:

```
if __name__ == '__main__':
    fetch_words()

```

### [5] Python Execution Model

Python Module

- Convenient import with API

Python Script

- Congvenient execution from the command line

Python Program

- Perhaps composed of many modules

### [5] Docstrings

Docstrings

- literal strings which document functions, modules, and classes
- they must be the first statement in the blocks for these constructs.
  ex:

```
def fetch_words(url):
    """Fetch a list of words from a URL.

        Args:
            url: The URL of a UTF-8 text document.

        Returns:
            A list of strings containing the words from the document.

    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words

```

- Module docstrings go at the top of the file
- useful params:
  - Usage
  - Args
  - Returns

Sphinx

- tool to create HTML documentation from Python docstrings.

### [5] Shebang

Shebang

- common on Unix-like systems for the start of a script to have a comment called a "shebang"
- e.g. `#!/usr/bin/env python`
- this allows the program loader to identify what interpreter to use to run this program
- also documents python version #
- typically in `env`

```
$ chmod +x words.py
$ ./sandbox.py http://sixty-north.com/c/t.txt
```

# [6] Objects and Types

### [6] getting Started = reassigning a variable

- setting `x = 10` sets the variable x to a `int 10` object in memory
- if after that, you call `x = 5`, a new object `int 5` gets created in memory and then x is assigned to it
- if `int 10` no longer has any references to its object, it is then garbage collected

- setting `y = x` sets y as a reference to the `int 5` object

`id()`

- returns a unique integer identifier for an object that is constant for the life of the object.
- `a is b` equality operator is used much more often

mutable objects

- lists are inherently mutable objects
- ex:

```
    r = [1, 2, 3]
    s = r
    s[1] = 4
    >>> r
    >>> [1, 4, 3]
```

- `def` is a statement executed at runtime

### [6] Passing Arguments

- Passing a variable as an argument passes through the inherent object, e.g.

```
x = [9, 15, 24]
def modify(k):
    k.append(65)

modify(x)

>>> at this point in time, the list object that is being reference by x has changed, making it now
    [9, 15, 24, 65]
```

- function arguments are trasnferred using pass-by-object-reference
- references to objects are copied, not the objects themselves

Optional Argument Values

- passed after default values
- can be passed either as `banner('Text', '*')`
- or more explicitly as `banner('Text', border='*')`
- with this you can pass them in any order like `banner(border='=', message='hello world')`

- however, because `def` statements are executed at runtime, any mutable optional argument objects, like lists, will only have that one reference
- for example,

```
def add_number_to_list(list=[]):
    list.append(5)

add_number_to_list()
>>> [5]

add_number_to_list()
>>> [5, 5]
```

- **always use immutable objects for default values**

```
def add_number_to_list(list=None):
    if list is None:
        list = []
    list.append(5)
    return list
```

### [6] Scopes in Python

4 Types of Scope in Python

- each is a context in which names are stored and can be looked up

1. Local - names inside current function (narrowest)
2. Enclosing - inside enclosing functions
3. Global - at the top level of the module
4. Built-in - in the special `builtins` module

Rebinding Global Names

```
count = 0

def set_count(c):
    count = c

set_count(5)
>>> 0
```

- notice how global count isn't set to 5 even that's the only scoped reference
- instead...

```
count = 0

def set_count(c):
    global count
    count = c

set_count(5)

>>> 5
```

### [6] Everything is An Object

```
import words
type(words)
>>> <class 'module'>
```

```
dir(words)
>>> ['__builtins__, '__file__', 'fetch_words', 'main']...etc.
```

### [7] Tuples

tuple

- immutable sequences of arbitrary objects
- similar syntax to lists

`t = ('Norway', 4.954, 3)`
`t[0] = 'Norway'`
`t[2] = 3`

- iterable with for loops
- concat-able with +
- nested tuples are permitted as well
- `h = (401)`
  - doesn't work with integers, need trailing comma separator to denote tuple instead of being interpreted as math
- `h = (401,)` => Parsed as single element tuple
- `e = ()` defines empty tuple

Tuple Unpacking

- destructuring operation that unpacks data structures into named references
  ex:

```
lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
lower
>>> 31
upper
>>> 86

OR

(a, (b, (c, d))) = (4, (3, (2, 1)))

a
>>> 4
b
>>> 3
...etc
```

Swapping

```
a = 'jelly'
b = 'bean'

a, b = b, a

a
>>> bean
b
>> jelly
```

`tuple([5, 4, 3])` coerces value into tuple
`5 in (3, 5, 6)` >>> True
`5 not in (3, 5, 6)` >>> False

### [6] Strings 2: Electric Boogaloo

- `_` variable definition used for unreferenced values

.format

- can use `.format` on string to replace vals inside string
- ex: `"The age of {0} is {1}".format('Jim', 32)` >>> "The age of Jim is 32"
- ex: `"Current position is {latitude} : {longitude}".format(latitude="60N", longitude="5E")`
- ex: `"You can display val 1: {} and val 2: {}".format(4, 23)`
- ex: `"Current position is x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2, 32, 82.3))`
- ex: `"Math constants: pi={m.pi}, e={m.e}".format(m=math)`

f-strings

- embed expressions inside literal strings using minimal syntax
- `f"one plus one is {1 + 1}"` => curly braces inserted and evaluated at runtime
- `f"{expr!r}"` =>

[7] Ranges

Range

- sequence representing an arithmetic progression of integers
- ex `range(5)` => `range(0, 5)`
- ex `for i in range(5)` => `0, 1, 2, 3, 4`
- ex `list(range(5, 10))` => `[5, 6, 7, 8, 9]`
- ex `list(range(0, 10, 2))` => `[0, 2, 4, 6, 8]`

Enumerate function

- constructs an iterable of (index, value) tuples around another iterable object
- ex:

```
t = [5, 6, 10, 12]
for p in enumerate(t):
    print(p)

>>>
(0, 5)
(1, 6)
...etc
```

or

```
for i, v in enumerate(t):
    print(f"i = {i}, v = {v})

>>>
i = 0, v = 5
i = 1, v = 6
...etc
```

[7] Lists

negative indices

- index from the end of sequences using negative numbers
- ex: `a = [0, 2]` `a[-1]` = 2

slicing

- ex: `a = [0, 1, 2, 3, 4]` `a[1:3]` => `[1, 2, 3]`
- ex: `a = [4, 5, 8, 9]` `a[1:-1]` => `[5, 8]`
- ex: `a[1:]` => `[5, 8, 9]`
- ex: `a[:2]` => `[4, 5, 8]`

`list.index()` === array.find()
`val in list` === array.includes()

del

- remove element from a list by index

`list.remove(<val>`

- remove element from a list by value

`list.insert(idx, val)` = `array.splice`

`list.reverse()` and `list.sort(reverse=<bool>, key=<callable object>)`

- changes list in place
- callable object ex: `len` => sorts by length of string
-

`sorted()` and `reversed()` exist as well, but return new copy
ex:

```
x = [5, 9, 2, 1]
y = sorted(x)
y
>>> [1, 2, 5, 9]
```

# [7] Built in Collections

### [7] Dictionaries

- basically just objects
- can use `dict` constructor to coerce other types into dictionaries, e.g.

`names = [('Alice', 32), ('Bob', 48)]`
`dict(names)` => `{ Alice: 32, Bob: 48 }

- or you can pass keyword arguments to dict
- ex: `b = dict(a=1, b=2)`
- dictionary copying is shallow
- `b.copy()`
- `dict.update()` - adds entries from one dictionary into another
- ex: `b.update({ c: 3, d: 4})` => `b = { a: 1, b: 2, c: 3, d: 4}`

- `dict.items()` - iterates over keys and values in tandem
- yields a (key, value) tuple on each iteration
- ex: `for key, value in colors.items():`

- `del` for deleting keys

### [7] Sets

- unordered collection of unique elements
- mutable
- elements in a set must be immutable
- ex: `p = { 6, 28, 596, 8128 }`
  - `type(p) <class 'set'>`
- `e = set([2, 4, 15, 54, 409])`
  - duplicate items are removed
  - order is arbitrary
- `in`, `not in` operators for checking
- `e.add(53)` for adding values
- `e.update([1, 2, 3])` for adding group of values
- `e.remove(2)` cares if element is member of set (get error if DNE)
- `e.discard(2)` does not care if element is member of set
- `e.copy()` for copying

- set algebra operations
  - union, difference, intersections
    - `union`: and/or items existing in two sets (returns 1 version of each shared item, and then everything else from each)
    - `intersection`: only shared items existing in two sets
    - `set1.union(set2)`, `set1.intersection(set2)`
    - `difference`: items existing in invoked set, but not the set its called on
      - ex: `set1.difference(set2)` => returns all set1 items that don't exist in set2
    - `symmetric_difference`: returns items from both lists that don't exist in the other
  - subset, superset, disjoint relations
    - `subset`: checks that all elements of first set are also present in second set
    - `issuperset`:` checks that all elements of second set are also present in first set
    - `isdisjoint`: if two sets have no members in common

### [7] Protocols

- A set of operations that a type must support to implement the protocol
- do not need to be defined as interfaces or base classes
- types only need to provide functioning implementations

```
Protocol            Implementing Collections
-----------------------------------------------------------------
Container           str, list, dict, range, tuple, set, bytes
Sized               str, list, dict, range, tuple, set, bytes
Iterable            str, list, dict, range, tuple, set, bytes
Sequence            str, list, range, tuple, bytes
Mutable Sequence    list
Mutable Set         set
Mutable Mapping     dict
```

ex: container must have `in` and `not in` be supported
ex: `len(container)` is required for calling something sized
ex: iterables provide means by reaching elements one by one (can be for-looped)
ex: sequence - items that can be reaches by index `item = sequence[index]` - items can be counted - items can be reversed - must also support iterable, sized, and container
