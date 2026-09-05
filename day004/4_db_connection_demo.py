"""Use both context-manager versions from db_connection.py."""

from db_connection import DBConnection, db_connection_cm, initialize_sample_table

DB_PATH = "demo.db"

initialize_sample_table(DB_PATH)

print("--- Inserting data (class-based context manager) ---")
with DBConnection(DB_PATH) as cursor:
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Aarav", "aarav@example.com"))
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Isha", "isha@example.com"))
print("\n--- Reading data back ---")
with DBConnection(DB_PATH) as cursor:
    cursor.execute("SELECT id, name, email FROM users")
    for row in cursor.fetchall():
        print(row)


print("\n--- Inserting data (function-based context manager) ---")
with db_connection_cm(DB_PATH) as cursor:
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Rohan", "rohan@example.com"))


print("\n--- Demonstrating rollback on error ---")
try:
    with DBConnection(DB_PATH) as cursor:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Meera", "meera@example.com"))
        raise ValueError("Simulated failure after insert")
except ValueError as e:
    print("Caught expected error:", e)

print("\n--- Final data (Meera should be missing) ---")
with DBConnection(DB_PATH) as cursor:
    cursor.execute("SELECT id, name, email FROM users")
    for row in cursor.fetchall():
        print(row)
