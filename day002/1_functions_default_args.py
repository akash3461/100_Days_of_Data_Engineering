"""
Script 1: Functions & Default Arguments
Topics: Functions, default args, *args, **kwargs
"""

# Basic function with a default argument
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Aarav"))                # uses default greeting
print(greet("Sara", "Welcome"))      # overrides default


# Function with multiple default args
def calculate_price(price, tax_rate=0.18, discount=0):
    final = price + (price * tax_rate) - discount
    return round(final, 2)

print(calculate_price(1000))                 # uses default tax, no discount
print(calculate_price(1000, discount=50))    # keyword arg used directly
print(calculate_price(1000, 0.05, 100))      # positional override


# *args -> accept any number of positional arguments
def total_marks(*scores):
    return sum(scores)

print("Total:", total_marks(80, 90, 70, 60))


# **kwargs -> accept any number of keyword arguments
def student_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_profile(name="Isha", age=21, course="Python")


# Combining normal args, default args, *args, **kwargs
def build_report(title, author="Unknown", *sections, **meta):
    print(f"\nReport: {title} by {author}")
    print("Sections:", sections)
    print("Meta info:", meta)

build_report("Sales Report", "Rohan", "Intro", "Data", "Conclusion", year=2026, dept="Finance")
