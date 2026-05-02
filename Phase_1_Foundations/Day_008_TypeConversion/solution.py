# Day 8 — Solutions

# Challenge 1: Convert string to int, add 50
result = int("100") + 50
print(result)   # 150

# Challenge 2: Add two user inputs correctly
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)

# Challenge 3: Price with 15% tip
price = float(input("Enter price: "))
tip = price * 0.15
total = price + tip
print("Tip:", round(tip, 2))
print("Total:", round(total, 2))

# Challenge 4: int() truncates, does not round
print(int(3.9))   # 3 — not 4! int() chops off the decimal
print(int(3.1))   # 3 — same result; it always truncates toward zero

# Challenge 5: Age in multiple types
birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year

age_int = int(age)
age_float = float(age)
age_str = str(age)

print(age_int, type(age_int))
print(age_float, type(age_float))
print(age_str, type(age_str))
