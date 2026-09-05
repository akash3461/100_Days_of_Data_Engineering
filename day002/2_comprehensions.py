"""Practice list and dictionary comprehensions."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n ** 2 for n in numbers]
print("Squares:", squares)

evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Labels:", labels)

words = ["python", "is", "fun", "and", "powerful"]
lengths = [len(word) for word in words]
print("Word lengths:", lengths)

uppercase_long_words = [word.upper() for word in words if len(word) > 3]
print("Long words uppercased:", uppercase_long_words)


word_lengths = {word: len(word) for word in words}
print("\nWord length dict:", word_lengths)

short_words = {word: len(word) for word in words if len(word) <= 3}
print("Short words only:", short_words)

names = ["Aarav", "Isha", "Rohan"]
scores = [85, 92, 78]
name_score_map = {name: score for name, score in zip(names, scores)}
print("\nName-score map:", name_score_map)

inverted = {score: name for name, score in name_score_map.items()}
print("Inverted map:", inverted)

table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("\nMultiplication table (3x3):")
for row in table:
    print(row)
