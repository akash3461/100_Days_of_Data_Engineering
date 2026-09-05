"""Summarize a list of numbers using common collection types."""

numbers = [12, 45, 23, 45, 67, 12, 89, 34, 23, 90, 15, 45]

print("Original list:", numbers)
print("Length:", len(numbers))

unique_numbers = set(numbers)
print("\nUnique numbers (set):", unique_numbers)

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("\nFrequency count:")
for num, count in frequency.items():
    print(f"  {num} -> {count} time(s)")

evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("\nEven numbers:", evens)
print("Odd numbers:", odds)

smallest = numbers[0]
largest = numbers[0]
index = 1

while index < len(numbers):
    if numbers[index] < smallest:
        smallest = numbers[index]
    elif numbers[index] > largest:
        largest = numbers[index]
    index += 1

print(f"\nSmallest: {smallest}, Largest: {largest}")

summary = (len(numbers), len(unique_numbers), smallest, largest, sum(numbers))
print("\nSummary tuple (total, unique, min, max, sum):", summary)

average = sum(numbers) / len(numbers)
if average > 40:
    print(f"\nAverage is {average:.2f} - that's on the higher side.")
else:
    print(f"\nAverage is {average:.2f} - that's on the lower side.")
