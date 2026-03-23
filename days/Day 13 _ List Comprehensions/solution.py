# Day 13 — List Comprehensions — SOLUTIONS

# Exercise 1
result = [x for x in range(1, 101) if x % 3 == 0 and x % 9 != 0]
print(result)

# Exercise 2
celsius = [0, 20, 37, 100, -10]
fahrenheit = [round(c * 9/5 + 32, 1) for c in celsius]
print(fahrenheit)

# Exercise 3
def count_chars(s: str) -> dict:
    # set(s) gives unique chars, then count each one
    return {char: s.count(char) for char in set(s)}
