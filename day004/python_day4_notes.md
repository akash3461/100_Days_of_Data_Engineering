# Python Day 4 — Recap Notes (OOP & Reusable Code)

## 1. Classes
- A **class** is a blueprint for creating objects — it defines what data (attributes) and behavior (methods) the objects will have.
```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"
```
- Nothing actually exists yet until you create an **object** from the class.

## 2. Objects
- An **object** is a specific instance created from a class. Each object has its own copy of the instance attributes.
```python
s1 = Student("Aarav")
s2 = Student("Isha")

s1.greet()   # "Hi, I'm Aarav"
s2.greet()   # "Hi, I'm Isha"
```
- `s1` and `s2` are both `Student` objects, but they hold different data.

## 3. `__init__`
- The **constructor** method — runs automatically the moment an object is created.
- `self` refers to the specific object being built; every method needs `self` as its first parameter.
```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand   # instance attribute
        self.year = year
```
- Whatever you assign to `self.x` inside `__init__` becomes that object's data, accessible later as `object.x`.

## 4. Inheritance
- Lets one class (**child**) reuse and extend the code of another class (**parent**).
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):          # Dog inherits from Animal
    def speak(self):        # overriding the parent's method
        return "Woof!"
```
- `super()` calls the parent class's version of a method — useful inside `__init__` or when extending (not fully replacing) behavior.
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # reuse parent's setup
        self.team_size = team_size
```
- Multi-level inheritance: a class can inherit from a class that already inherits from something else (`SeniorDeveloper → Developer → Employee`).

## 5. Encapsulation
- **Hiding internal data** and only exposing controlled ways to access/change it.
- Naming conventions:
  - `self.name` → public, accessible from anywhere.
  - `self._name` → protected (convention only — "please don't touch this directly").
  - `self.__name` → private (name-mangled, harder to access accidentally from outside).
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # private

    def get_balance(self):            # controlled read access
        return self.__balance

    def deposit(self, amount):        # controlled write access, with validation
        if amount > 0:
            self.__balance += amount
```
- Cleaner alternative: `@property` lets you write `object.attribute` syntax while still running validation behind the scenes.
```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Too cold to exist")
        self.__celsius = value
```

## 6. Context Managers (`with` statement) — DB Connection Example
- A **context manager** guarantees setup and cleanup code always run together — even if an error happens in between. Most common use: files, database connections, network sockets.
- **Class-based** — implement `__enter__` (setup) and `__exit__` (cleanup):
```python
class DBConnection:
    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.connection.commit()   # no error -> save changes
        else:
            self.connection.rollback() # error -> undo changes
        self.connection.close()
        return False   # don't swallow the exception
```
- **Function-based** — same idea, using `@contextlib.contextmanager`:
```python
from contextlib import contextmanager

@contextmanager
def db_connection_cm(db_path):
    connection = sqlite3.connect(db_path)
    try:
        yield connection.cursor()   # code before yield = setup
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()          # code after yield = cleanup, always runs
```
- Usage is identical either way:
```python
with DBConnection("my.db") as cursor:
    cursor.execute("INSERT INTO users VALUES (...)")
# connection is guaranteed to close here, commit on success, rollback on error
```
- This is exactly why `with open(file) as f:` works the way it does — files are context managers too.

---

## Quick Reference Table

| Concept | Keyword/Syntax | Purpose |
|---|---|---|
| Class | `class Name:` | Blueprint for objects |
| Object | `obj = ClassName(...)` | A specific instance with its own data |
| Constructor | `__init__(self, ...)` | Runs on creation, sets initial data |
| Inheritance | `class Child(Parent):` | Reuse/extend another class's code |
| Method override | redefine method in child | Custom behavior for the child class |
| `super()` | `super().__init__(...)` | Call the parent's version of a method |
| Encapsulation | `_protected`, `__private` | Hide/control access to internal data |
| Property | `@property` / `@x.setter` | Attribute-like access with validation |
| Context manager (class) | `__enter__` / `__exit__` | Guaranteed setup + cleanup |
| Context manager (function) | `@contextmanager` + `yield` | Same guarantee, shorter syntax |

---

## One-Line Takeaways
- **Class** → the blueprint. **Object** → the actual thing built from it.
- **`__init__`** → runs once, right when an object is born.
- **Inheritance** → don't repeat yourself; extend what already exists.
- **Encapsulation** → hide the mess, expose a clean interface.
- **Context managers** → "always clean up, no matter what happens."

## Practice Reminder
Match each script to the concept:
1. `classes_objects.py` → classes, objects, `__init__`, instance vs. class attributes
2. `inheritance.py` → parent/child classes, `super()`, method overriding, multi-level inheritance
3. `encapsulation.py` → public/protected/private attributes, getters/setters, `@property`
4. `db_connection.py` → the reusable module: `DBConnection` (class-based) and `db_connection_cm` (function-based) context managers
5. `db_connection_demo.py` → shows the module in action: insert, read, and a rollback-on-error demonstration

Keep `db_connection.py` alongside `db_connection_demo.py` when running it — the demo imports directly from that module, which is the point: it's meant to be reused across projects, not copy-pasted each time.
