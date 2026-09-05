"""Look up contacts and group them by city."""

contacts = {
    "Anil": ("9876543210", "Mumbai"),
    "Sneha": ("9123456780", "Delhi"),
    "Farhan": ("9988776655", "Pune"),
    "Divya": ("9090909090", "Mumbai"),
}

print("All Contacts")
print("-" * 40)
for name, details in contacts.items():
    phone, city = details
    print(f"{name:<10} | Phone: {phone} | City: {city}")

search_name = "Farhan"
print("\nSearching for:", search_name)

if search_name in contacts:
    phone, city = contacts[search_name]
    print(f"Found! {search_name} lives in {city}, phone: {phone}")
else:
    print(f"{search_name} not found in contacts.")

city_groups = {}

for name, (phone, city) in contacts.items():
    if city not in city_groups:
        city_groups[city] = []
    city_groups[city].append(name)

print("\nContacts grouped by city:")
for city, names in city_groups.items():
    print(f"{city}: {names}")
