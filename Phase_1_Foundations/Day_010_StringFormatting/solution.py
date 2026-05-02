# Day 10 — Solutions

# Challenge 1: Name and age f-string
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

# Challenge 2: Price formatted to 2 decimal places with currency prefix
price = float(input("Enter a price: "))
print(f"R{price:.2f}")

# Challenge 3: Format a decimal as a percentage
ratio = float(input("Enter a decimal value (e.g. 0.85 for 85%): "))
print(f"{ratio:.2%}")

# Challenge 4: Right-aligned receipt row
item = "Coffee"
qty = 2
unit_price = 35.5
print(f"{'Item':<20} {'Qty':>5} {'Price':>8}")
print(f"{item:<20} {qty:>5} {unit_price:>8.2f}")

# Challenge 5: Formatted name badge
name = input("Enter your name: ")
role = input("Enter your role: ")
print("------------------------------")
print(f"|{name:^28}|")
print(f"|{role:^28}|")
print("------------------------------")
