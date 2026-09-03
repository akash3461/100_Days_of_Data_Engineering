"""
Script 3: Shopping Cart Bill Calculator
Topics used: Lists, Dictionaries, Loops (while), Conditionals (if/else)
"""

# Dictionary acting as a mini "price catalog"
price_catalog = {
    "apple": 40,
    "milk": 55,
    "bread": 35,
    "rice": 70,
    "eggs": 6,
}

cart = []  # LIST to store items added by the user

print("Available items and price (per unit/kg):")
for item, price in price_catalog.items():
    print(f" - {item}: Rs.{price}")

i = 0
item_names = ["apple", "milk", "bread", "eggs"]  # simulated user input list

# WHILE loop to simulate adding items one by one
while i < len(item_names):
    item = item_names[i]

    # Conditional check if item exists in catalog
    if item in price_catalog:
        cart.append(item)
        print(f"Added '{item}' to cart.")
    else:
        print(f"Sorry, '{item}' is not available.")

    i += 1

# Calculate total bill
total_bill = 0
item_count = {}  # dictionary to count repeated items

for product in cart:
    total_bill += price_catalog[product]
    item_count[product] = item_count.get(product, 0) + 1

print("\nFinal Bill")
print("-" * 25)
for product, qty in item_count.items():
    line_total = price_catalog[product] * qty
    print(f"{product:<10} x{qty}  = Rs.{line_total}")

print("-" * 25)
print(f"Total: Rs.{total_bill}")

# Conditional for discount
if total_bill > 100:
    print("You got a 10% discount!")
    total_bill *= 0.9
    print(f"Final Amount: Rs.{total_bill:.2f}")
