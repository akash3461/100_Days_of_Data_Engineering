"""
Script 6: Number List Analyzer (Combines everything)
Topics used: Lists, Tuples, Sets, Dictionaries, Conditionals, Loops (for & while)
"""

numbers = [12, 45, 23, 45, 67, 12, 89, 34, 23, 90, 15, 45]

# 1. LIST basics
print("Original list:", numbers)
print("Length:", len(numbers))

# 2. Remove duplicates using a SET
unique_numbers = set(numbers)
print("\nUnique numbers (set):", unique_numbers)

# 3. Count frequency of each number using a DICTIONARY
frequency = {}
for num in numbers:  # LOOP
    frequency[num] = frequency.get(num, 0) + 1

print("\nFrequency count:")
for num, count in frequency.items():
    print(f"  {num} -> {count} time(s)")

# 4. Separate even and odd numbers into two lists using CONDITIONALS
evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("\nEven numbers:", evens)
print("Odd numbers:", odds)

# 5. Find min and max using a WHILE loop
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

# 6. Store final summary as a TUPLE (immutable result record)
summary = (len(numbers), len(unique_numbers), smallest, largest, sum(numbers))
print("\nSummary tuple (total, unique, min, max, sum):", summary)

# 7. Simple report using conditional
average = sum(numbers) / len(numbers)
if average > 40:
    print(f"\nAverage is {average:.2f} — that's on the higher side.")
else:
    print(f"\nAverage is {average:.2f} — that's on the lower side.")
