# Python Day 2 — Recap Notes

## 1. Functions & Default Arguments
- A **function** is a reusable block of code, defined with `def`.
- A **default argument** provides a fallback value if the caller doesn't pass one.
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Aarav")             # uses default -> "Hello, Aarav!"
greet("Sara", "Welcome")   # overrides default
```
- `*args` → collects extra **positional** arguments into a tuple.
- `**kwargs` → collects extra **keyword** arguments into a dict.
```python
def total(*scores):        # scores = (80, 90, 70)
    return sum(scores)

def profile(**info):       # info = {"name": "Isha", "age": 21}
    print(info)
```

## 2. List & Dict Comprehensions
- A **shorter way** to build lists/dicts instead of writing a full `for` loop.

**List comprehension:**
```python
squares = [n ** 2 for n in range(5)]          # [0,1,4,9,16]
evens = [n for n in range(10) if n % 2 == 0]  # filter
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]  # transform
```

**Dict comprehension:**
```python
lengths = {word: len(word) for word in ["hi", "python"]}
# {'hi': 2, 'python': 6}
```
- Pattern: `[expression for item in iterable if condition]`

## 3. Modules & Imports
- A **module** is just a `.py` file with reusable code.
```python
import math                    # full import
math.sqrt(16)

from random import randint     # import specific function
randint(1, 10)

import datetime as dt          # import with alias
dt.date.today()

import helper_module           # import your own file
helper_module.add(2, 3)
```
- Rule: to import your own module, it must be in the same folder (or Python's path).

## 4. Exception Handling (try/except)
- Prevents the program from crashing when something goes wrong.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Ran only if NO error happened")
finally:
    print("Always runs, error or not")
```
- Catch specific errors (`ValueError`, `KeyError`, `TypeError`) before a general `Exception`.
- Use `raise` to trigger your own errors:
```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

## 5. Reading & Writing Files
- Always use `with open(...)` — it auto-closes the file safely.
```python
with open("file.txt", "w") as f:
    f.write("Hello\n")

with open("file.txt", "r") as f:
    content = f.read()          # whole file
    # or
    for line in f:              # line by line
        print(line.strip())
```
- Modes: `"r"` read, `"w"` write (overwrites), `"a"` append, `"r+"` read+write.

## 6. Clear, Clean I/O Functions (Production-Style)
- Break a task into **small functions, each with ONE job**:
  - one function only **reads** data
  - one function only **cleans** a value
  - one function only **writes** output
- This makes code easier to test, debug, and reuse.
```python
def read_csv_file(path): ...     # only reads
def clean_row(row): ...          # only cleans
def write_clean_csv(path, data): ...  # only writes
```
- Handle missing/invalid values with safe defaults instead of letting the program crash:
```python
def clean_number(value, value_type=int, default=None):
    try:
        return value_type(value.strip())
    except (ValueError, AttributeError):
        return default
```

---

## Quick Reference Table

| Concept | Keyword/Syntax | Purpose |
|---|---|---|
| Default args | `def f(x, y=10):` | Fallback value if not passed |
| *args / **kwargs | `def f(*a, **kw):` | Accept variable arguments |
| List comprehension | `[x for x in y if cond]` | Build a list in one line |
| Dict comprehension | `{k: v for k, v in items}` | Build a dict in one line |
| Import module | `import x` / `from x import y` | Reuse code from other files |
| try/except | `try: ... except X:` | Handle errors gracefully |
| finally | `finally:` | Always runs (cleanup code) |
| File read | `with open(f, "r") as file:` | Read data safely |
| File write | `with open(f, "w") as file:` | Write data safely |

---

## One-Line Takeaways
- **Default args** → "use this value unless told otherwise."
- **Comprehensions** → shortcut for building lists/dicts from loops.
- **Modules** → don't reinvent the wheel, import it.
- **try/except** → expect things to fail, handle it gracefully.
- **File I/O** → always use `with`, never forget to close manually.
- **Clean functions** → one function, one job (read OR clean OR write, never all three).

## Practice Reminder
Match each script to the concept:
1. `functions_default_args.py` → functions, default args, *args/**kwargs
2. `comprehensions.py` → list & dict comprehensions
3. `modules_imports.py` → built-in + custom module imports
4. `exception_handling.py` → try/except/else/finally, raise
5. `file_read_write.py` → reading & writing text/CSV files
6. `csv_parser_capstone.py` → everything combined: reads raw_data.csv,
   cleans missing/invalid values (blank names, bad ages like "twenty",
   missing salaries), and writes clean_data.csv
