"""
Script 1: Word Frequency Counter
Topics used: Lists, Dictionaries, Loops (for), Conditionals (if)
"""

def count_word_frequency(text):
    # Step 1: Clean and split text into a list of words
    words = text.lower().split()  # LIST created here

    # Step 2: Create an empty dictionary to store word counts
    frequency = {}  # DICTIONARY

    # Step 3: Loop through each word in the list
    for word in words:
        # Remove simple punctuation
        word = word.strip(".,!?;:\"'")

        if word == "":
            continue  # skip empty strings

        # Conditional: check if word already exists as a key
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def display_frequency(frequency):
    print("\nWord Frequency Report")
    print("-" * 30)
    # Loop through dictionary items
    for word, count in frequency.items():
        print(f"{word:<15} : {count}")


# ---- Main Program ----
sample_text = """Python is great. Python is easy to learn.
Learning Python is fun, and Python is powerful."""

result = count_word_frequency(sample_text)
display_frequency(result)

# Bonus: Find the most frequent word using a loop + conditional
most_common_word = None
highest_count = 0

for word, count in result.items():
    if count > highest_count:
        highest_count = count
        most_common_word = word

print("\nMost frequent word:", most_common_word, f"({highest_count} times)")
