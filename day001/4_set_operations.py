"""Use set operations to compare two friends lists."""

raj_friends = ["Amit", "Sara", "John", "Meera", "Kabir"]
priya_friends = ["Sara", "John", "Divya", "Kabir", "Neha"]

raj_set = set(raj_friends)
priya_set = set(priya_friends)

common_friends = raj_set & priya_set
print("Common friends of Raj and Priya:")
for friend in common_friends:
    print(" -", friend)

only_raj = raj_set - priya_set
print("\nFriends only Raj has:")
for friend in only_raj:
    print(" -", friend)

only_priya = priya_set - raj_set
print("\nFriends only Priya has:")
for friend in only_priya:
    print(" -", friend)

all_friends = raj_set | priya_set
print(f"\nTotal unique friends combined: {len(all_friends)}")
print(sorted(all_friends))

check_name = "Sara"
if check_name in all_friends:
    print(f"\n'{check_name}' is in the combined friend circle.")
else:
    print(f"\n'{check_name}' is not in the combined friend circle.")
