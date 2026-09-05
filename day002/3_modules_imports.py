"""A few ways to import code from Python modules."""

import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

from random import randint, choice
print("Random number (1-10):", randint(1, 10))
print("Random choice:", choice(["apple", "banana", "mango"]))

import datetime as dt
today = dt.date.today()
print("Today's date:", today)

import helper_module

print("\nUsing our custom module:")
print("Add:", helper_module.add(5, 7))
print("Circle area (r=3):", helper_module.circle_area(3))
print(helper_module.greet("Meera"))

from helper_module import PI, greet
print("\nDirect import PI:", PI)
print(greet("Kabir"))
