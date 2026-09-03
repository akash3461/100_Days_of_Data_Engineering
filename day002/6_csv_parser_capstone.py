"""
Script 6 (Capstone): Raw CSV Parser & Cleaner
Topics combined: Functions & default args, comprehensions, modules (csv),
                  exception handling, file I/O, clean-I/O function design

Goal: Read a messy CSV, clean whitespace, handle missing/invalid values,
      and return clean structured data (list of dicts).
"""

import csv   # built-in module import


# ---------- Clear, single-purpose I/O functions ----------

def read_csv_file(filepath):
    """Reads a CSV file and returns a list of raw dict rows.
    Keeps this function's ONLY job as reading — no cleaning here."""
    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader]   # list comprehension
        return rows
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []


def clean_string(value):
    """Strips whitespace; returns None for empty strings."""
    if value is None:
        return None
    value = value.strip()
    return value if value != "" else None


def clean_number(value, value_type=int, default=None):
    """Safely converts a string to int/float, using try/except.
    Returns `default` if conversion fails or value is missing."""
    value = clean_string(value)
    if value is None:
        return default
    try:
        return value_type(value)
    except ValueError:
        return default


def clean_row(raw_row):
    """Takes one raw CSV row (dict) and returns a cleaned dict.
    This is the 'clear function' that does ONE job: cleaning."""
    # Keys may have leading/trailing spaces too (from header), so normalize
    normalized = {key.strip(): value for key, value in raw_row.items()}

    cleaned = {
        "name": clean_string(normalized.get("Name")) or "Unknown",
        "age": clean_number(normalized.get("Age"), int, default=None),
        "city": clean_string(normalized.get("City")) or "Not Provided",
        "salary": clean_number(normalized.get("Salary"), float, default=0.0),
    }
    return cleaned


def clean_dataset(raw_rows):
    """Cleans an entire list of raw rows using clean_row().
    Uses a list comprehension to keep it short and readable."""
    return [clean_row(row) for row in raw_rows]


def write_clean_csv(filepath, cleaned_rows):
    """Writes cleaned data back out to a new CSV file."""
    if not cleaned_rows:
        print("No data to write.")
        return

    try:
        with open(filepath, "w", newline="") as f:
            fieldnames = cleaned_rows[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(cleaned_rows)
        print(f"Clean data written to '{filepath}'.")
    except Exception as e:
        print(f"Error writing file: {e}")


def summarize(cleaned_rows):
    """Quick summary report using comprehensions + built-ins."""
    valid_ages = [row["age"] for row in cleaned_rows if row["age"] is not None]
    valid_salaries = [row["salary"] for row in cleaned_rows if row["salary"] > 0]

    print("\n----- Data Summary -----")
    print("Total rows:", len(cleaned_rows))
    print("Rows with valid age:", len(valid_ages))
    print("Rows with valid salary:", len(valid_salaries))
    if valid_ages:
        print(f"Average age: {sum(valid_ages) / len(valid_ages):.1f}")
    if valid_salaries:
        print(f"Average salary: {sum(valid_salaries) / len(valid_salaries):.2f}")


# ---------- Main program ----------

def main():
    input_file = "raw_data.csv"
    output_file = "clean_data.csv"

    raw_rows = read_csv_file(input_file)

    if not raw_rows:
        print("No data loaded. Exiting.")
        return

    print("Raw rows loaded:", len(raw_rows))

    cleaned_rows = clean_dataset(raw_rows)

    print("\n----- Cleaned Data -----")
    for row in cleaned_rows:
        print(row)

    write_clean_csv(output_file, cleaned_rows)
    summarize(cleaned_rows)


if __name__ == "__main__":
    main()
