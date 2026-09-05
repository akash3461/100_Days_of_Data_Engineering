"""Count how often each word appears in a piece of text."""

def count_word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?;:\"'")

        if word == "":
            continue

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def display_frequency(frequency):
    print("\nWord Frequency Report")
    print("-" * 30)
    for word, count in frequency.items():
        print(f"{word:<15} : {count}")


sample_text = """Python is great. Python is easy to learn.
Learning Python is fun, and Python is powerful."""

result = count_word_frequency(sample_text)
display_frequency(result)

most_common_word = None
highest_count = 0

for word, count in result.items():
    if count > highest_count:
        highest_count = count
        most_common_word = word

print("\nMost frequent word:", most_common_word, f"({highest_count} times)")
