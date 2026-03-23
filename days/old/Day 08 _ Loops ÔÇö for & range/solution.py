# Day 08 — Loops: for & range — SOLUTIONS

# Exercise 1 — multiplication table
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Exercise 2 — FizzBuzz
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 3 — sum without sum()
numbers = [10, 25, 3, 47, 8, 16]
total = 0
for n in numbers:
    total += n
print(f"Total: {total}")   # 109
