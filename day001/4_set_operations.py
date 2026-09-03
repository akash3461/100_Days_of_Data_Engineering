"""
Script 4: Common Friends Finder (Set Operations)
Topics used: Sets, Lists, Loops (for), Conditionals (if)
"""

# Two lists of friends for two people
raj_friends = ["Amit", "Sara", "John", "Meera", "Kabir"]
priya_friends = ["Sara", "John", "Divya", "Kabir", "Neha"]

# Convert lists to SETS to use set operations
raj_set = set(raj_friends)
priya_set = set(priya_friends)

# Common friends (intersection)
common_friends = raj_set & priya_set
print("Common friends of Raj and Priya:")
for friend in common_friends:
    print(" -", friend)

# Friends only Raj has (difference)
only_raj = raj_set - priya_set
print("\nFriends only Raj has:")
for friend in only_raj:
    print(" -", friend)

# Friends only Priya has (difference)
only_priya = priya_set - raj_set
print("\nFriends only Priya has:")
for friend in only_priya:
    print(" -", friend)

# All friends combined (union), no duplicates
all_friends = raj_set | priya_set
print(f"\nTotal unique friends combined: {len(all_friends)}")
print(sorted(all_friends))

# Conditional check using 'in' with a set (fast lookup)
check_name = "Sara"
if check_name in all_friends:
    print(f"\n'{check_name}' is in the combined friend circle.")
else:
    print(f"\n'{check_name}' is not in the combined friend circle.")
