# Day 07 — Loops: while — SOLUTIONS

# Countdown
n = 10
while n >= 1:
    print(n)
    n -= 1
print("Blast off!")

# Sum until done
total = 0
while True:
    entry = input("Number (or 'done'): ")
    if entry == 'done': break
    total += float(entry)
print(f"Total: {total}")

# Number guessing game
secret = 7
attempts = 0
while True:
    guess = int(input("Guess: "))
    attempts += 1
    if guess > secret:   print("Too high")
    elif guess < secret: print("Too low")
    else:
        print(f"Correct! in {attempts} attempts")
        break
