"""Read, write, append, and inspect a couple of simple files."""

lines_to_write = ["Python is fun\n", "File handling is useful\n", "Practice makes perfect\n"]

with open("sample_notes.txt", "w") as f:
    f.writelines(lines_to_write)

print("File written successfully.")

with open("sample_notes.txt", "r") as f:
    content = f.read()
print("\nFull content:\n", content)

with open("sample_notes.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print("-", line.strip())

with open("sample_notes.txt", "a") as f:
    f.write("This line was appended.\n")

with open("sample_notes.txt", "r") as f:
    print("\nAfter appending:\n", f.read())

print("\nReading raw_data.csv manually:")
with open("raw_data.csv", "r") as f:
    header = f.readline().strip().split(",")
    print("Header:", header)

    for line in f:
        row = line.strip().split(",")
        print(row)

