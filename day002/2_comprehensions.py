"""
Script 2: List & Dict Comprehensions
Topics: List comprehensions, dict comprehensions, conditionals inside comprehensions
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic list comprehension: square each number
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# List comprehension with a condition (filter)
evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

# List comprehension with if/else (transform, not filter)
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Labels:", labels)

# Comprehension over strings
words = ["python", "is", "fun", "and", "powerful"]
lengths = [len(word) for word in words]
print("Word lengths:", lengths)

uppercase_long_words = [word.upper() for word in words if len(word) > 3]
print("Long words uppercased:", uppercase_long_words)


# --- Dict comprehensions ---

# Basic dict comprehension: word -> length
word_lengths = {word: len(word) for word in words}
print("\nWord length dict:", word_lengths)

# Dict comprehension with condition
short_words = {word: len(word) for word in words if len(word) <= 3}
print("Short words only:", short_words)

# Build a dict from two lists using zip + comprehension
names = ["Aarav", "Isha", "Rohan"]
scores = [85, 92, 78]
name_score_map = {name: score for name, score in zip(names, scores)}
print("\nName-score map:", name_score_map)

# Invert a dictionary using comprehension
inverted = {score: name for name, score in name_score_map.items()}
print("Inverted map:", inverted)

# Nested comprehension: build a multiplication table (list of lists)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("\nMultiplication table (3x3):")
for row in table:
    print(row)
