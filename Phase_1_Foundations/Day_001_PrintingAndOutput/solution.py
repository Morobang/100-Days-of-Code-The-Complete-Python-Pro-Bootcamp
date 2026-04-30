# Day 1 — Solutions

# Challenge 1: Print your name, age, and city on separate lines
print("Alex")
print(25)
print("Cape Town")

# Challenge 2: Print "Python" "is" "awesome" separated by spaces using sep
print("Python", "is", "awesome", sep=" ")

# Challenge 3: Print an address block using a single print() and \n
print("123 Main Street\nCape Town\nSouth Africa")

# Challenge 4: Loading sequence on one line using end=
print("Loading", end="... ")
print("10%", end="... ")
print("20%", end="... ")
print("30%", end="... ")
print("Done!")

# Challenge 5: Formatted receipt
print("========== RECEIPT ==========")
print(f"{'Item':<12}{'Price':>8}")
print(f"{'Coffee':<12}{'R25.00':>8}")
print(f"{'Sandwich':<12}{'R45.00':>8}")
print("=" * 30)
print(f"{'TOTAL':<12}{'R70.00':>8}")
