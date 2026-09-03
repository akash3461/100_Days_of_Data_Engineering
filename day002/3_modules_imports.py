"""
Script 3: Modules & Imports
Topics: Built-in module imports, custom module imports, import styles
"""

# 1. Importing a built-in module fully
import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# 2. Importing specific functions from a module
from random import randint, choice
print("Random number (1-10):", randint(1, 10))
print("Random choice:", choice(["apple", "banana", "mango"]))

# 3. Importing a module with an alias
import datetime as dt
today = dt.date.today()
print("Today's date:", today)

# 4. Importing our own custom module (helper_module.py must be in same folder)
import helper_module

print("\nUsing our custom module:")
print("Add:", helper_module.add(5, 7))
print("Circle area (r=3):", helper_module.circle_area(3))
print(helper_module.greet("Meera"))

# 5. Importing specific items from our custom module
from helper_module import PI, greet
print("\nDirect import PI:", PI)
print(greet("Kabir"))
