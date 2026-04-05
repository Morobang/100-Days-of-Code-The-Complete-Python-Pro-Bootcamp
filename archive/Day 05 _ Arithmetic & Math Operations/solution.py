# Day 05 — Arithmetic & Math Operations — SOLUTIONS

# Exercise 1 — tip calculator
bill = float(input("Bill total (R): "))
tip_pct = float(input("Tip %: "))
people = int(input("How many people? "))
total = bill * (1 + tip_pct / 100)
per_person = round(total / people, 2)
print(f"Each person pays: R{per_person}")

# Exercise 2 — even or odd
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

# Exercise 3 — coin counter
cents = 287
rands = cents // 100
remaining = cents % 100
print(f"R{rands} and {remaining} cents")
