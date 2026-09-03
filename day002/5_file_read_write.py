"""
Script 5: Reading & Writing Files
Topics: open(), read/write modes, with statement, reading line by line, writing files
"""

# --- Writing a text file ---
lines_to_write = ["Python is fun\n", "File handling is useful\n", "Practice makes perfect\n"]

with open("sample_notes.txt", "w") as f:
    f.writelines(lines_to_write)

print("File written successfully.")

# --- Reading the whole file at once ---
with open("sample_notes.txt", "r") as f:
    content = f.read()
print("\nFull content:\n", content)

# --- Reading line by line ---
with open("sample_notes.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print("-", line.strip())

# --- Appending to a file ---
with open("sample_notes.txt", "a") as f:
    f.write("This line was appended.\n")

with open("sample_notes.txt", "r") as f:
    print("\nAfter appending:\n", f.read())

# --- Reading a CSV file manually (without the csv module) ---
print("\nReading raw_data.csv manually:")
with open("raw_data.csv", "r") as f:
    header = f.readline().strip().split(",")
    print("Header:", header)

    for line in f:
        row = line.strip().split(",")
        print(row)

# Note: 'with' automatically closes the file, even if an error occurs.
# This is safer than manually calling f.close().
