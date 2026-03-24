# Day 04 — User Input & Type Casting — SOLUTIONS

# BMI
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
print(f"BMI: {round(weight / height**2, 1)}")

# Seconds
total   = int(input("Seconds: "))
h, m, s = total//3600, (total%3600)//60, total%60
print(f"{h}h {m}m {s}s")

# Name formatter
first = input("First name: ")
last  = input("Last name: ")
print(f"Full name: {last.upper()}, {first.capitalize()}")
