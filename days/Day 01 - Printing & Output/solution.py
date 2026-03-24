# Day 01 — Printing & Output — SOLUTIONS
# Read this ONLY after attempting the challenges yourself.

# Challenge 1
print("Rocket")
print("Pretoria")
print("Tekken 8")

# Challenge 2 — sep parameter
print(2025, 3, 21, sep="/")   # → 2025/3/21

# Challenge 3 — same line with two print() calls
print("Hello", end=" ")
print("World!")

# Challenge 4 — receipt with f-strings
item   = "Tekken 8"
price  = 1299
player = "Rocket"
print("===== RECEIPT =====")
print(f"Item:   {item}")
print(f"Price:  R{price}")
print(f"Player: {player}")
print("===================")
