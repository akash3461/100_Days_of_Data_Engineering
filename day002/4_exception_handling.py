"""Practice handling and raising common exceptions."""

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print(f"Attempted to divide {a} by {b}\n")

print(safe_divide(10, 2))
print(safe_divide(10, 0))


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number.")
        return None
    except TypeError:
        print(f"Cannot convert {type(value)} to int.")
        return None

print(convert_to_int("42"))
print(convert_to_int("abc"))
print(convert_to_int(None))


def risky_lookup(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Key '{key}' not found.")
        return "N/A"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

data = {"name": "Riya", "age": 21}
print(risky_lookup(data, "name"))
print(risky_lookup(data, "city"))


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("Caught custom error:", e)
