# Day 08 — Loops: for & range — SOLUTIONS

# Multiplication table
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

# FizzBuzz
for i in range(1, 31):
    if i % 15 == 0:   print('FizzBuzz')
    elif i % 3 == 0:  print('Fizz')
    elif i % 5 == 0:  print('Buzz')
    else:             print(i)

# Leaderboard
players = [('Rocket',9500),('Alice',8700),('Bob',10200)]
ranked = sorted(players, key=lambda p: p[1], reverse=True)
for i, (name, score) in enumerate(ranked, 1):
    print(f"{i}. {name} — {score}")
