"""Examples of default arguments, *args, and **kwargs."""

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Aarav"))
print(greet("Sara", "Welcome"))


def calculate_price(price, tax_rate=0.18, discount=0):
    final = price + (price * tax_rate) - discount
    return round(final, 2)

print(calculate_price(1000))
print(calculate_price(1000, discount=50))
print(calculate_price(1000, 0.05, 100))


def total_marks(*scores):
    return sum(scores)

print("Total:", total_marks(80, 90, 70, 60))


def student_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_profile(name="Isha", age=21, course="Python")


def build_report(title, author="Unknown", *sections, **meta):
    print(f"\nReport: {title} by {author}")
    print("Sections:", sections)
    print("Meta info:", meta)

build_report("Sales Report", "Rohan", "Intro", "Data", "Conclusion", year=2026, dept="Finance")
