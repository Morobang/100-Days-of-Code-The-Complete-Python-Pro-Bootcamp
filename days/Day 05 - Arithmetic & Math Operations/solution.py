# Day 05 — Arithmetic — SOLUTIONS

# Tip calculator
bill   = float(input("Bill: R"))
pct    = float(input("Tip %: "))
people = int(input("People: "))
share  = round(bill * (1 + pct/100) / people, 2)
print(f"Each person pays: R{share}")

# Even or odd
n = int(input("Number: "))
print("Even" if n % 2 == 0 else "Odd")

# Compound interest
p = float(input("Principal: R"))
r = float(input("Annual rate %: "))
t = int(input("Years: "))
a = round(p * (1 + r/100) ** t, 2)
print(f"After {t} years: R{a}")
