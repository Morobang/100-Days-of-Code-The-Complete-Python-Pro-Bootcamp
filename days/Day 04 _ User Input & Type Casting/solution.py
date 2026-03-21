# Day 04 — User Input & Type Casting — SOLUTIONS

# Exercise 1 — BMI calculator
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = round(weight / height ** 2, 1)
print(f"Your BMI is {bmi}")

# Exercise 2 — Name formatter
first = input("First name: ")
last = input("Last name: ")
print(f"Full name: {last.upper()}, {first.capitalize()}")

# Exercise 3 — Seconds converter
total = int(input("Enter seconds: "))
hours   = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
