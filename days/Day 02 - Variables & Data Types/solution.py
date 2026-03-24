# Day 02 — Variables & Data Types — SOLUTIONS

# Challenge 1
name      = "Rocket"
age       = 23
win_rate  = 0.72
is_ranked = True
print(f"name is a {type(name)}")
print(f"age is a {type(age)}")
print(f"win_rate is a {type(win_rate)}")
print(f"is_ranked is a {type(is_ranked)}")

# Challenge 2
score = "9500"
# input() always returns a string — int() converts it
final = int(score) + 500
print(f"Final score: {final}")

# Challenge 3 — the surprise
# bool("False") is True because "False" is a non-empty string
# Python doesn't interpret the string content — it only checks if it's empty

# Challenge 4 — swap without temp
a, b = "PS5", "Xbox"
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After:  a={a}, b={b}")
