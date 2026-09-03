"""
helper_module.py
A small custom module to demonstrate imports.
"""

PI = 3.14159

def add(a, b):
    return a + b

def circle_area(radius):
    return round(PI * radius ** 2, 2)

def greet(name):
    return f"Hi {name}, this greeting came from helper_module!"
