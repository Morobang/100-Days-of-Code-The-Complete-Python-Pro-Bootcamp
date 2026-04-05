# Day 07 — Loops: while — SOLUTIONS

# Exercise 1 — countdown
n = 10
while n >= 1:
    print(n)
    n -= 1
print("Blast off!")

# Exercise 2 — sum until done
total = 0
while True:
    entry = input("Enter a number (or 'done'): ")
    if entry == 'done':
        break
    total += float(entry)
print(f"Total: {total}")

# Exercise 3 — guess the number
secret = 7
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print(f"Correct! Took {attempts} attempts")
        break
