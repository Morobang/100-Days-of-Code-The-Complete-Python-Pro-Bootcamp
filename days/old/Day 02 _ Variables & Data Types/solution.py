# Day 02 — Variables & Data Types — SOLUTIONS

# Exercise 1
name = "Rocket"
age = 23
height = 1.75
owns_ps5 = True
print(name)
print(age)
print(height)
print(owns_ps5)

# Exercise 2
# score is a string — we need int() to convert it before doing math
score = "95"
result = int(score) + 5
print(result)   # → 100

# Exercise 3 — the surprise:
# bool("False") → True because "False" is a non-empty string
# Python doesn't know that "False" means the boolean False
w = bool("False")
print(w)   # True!
