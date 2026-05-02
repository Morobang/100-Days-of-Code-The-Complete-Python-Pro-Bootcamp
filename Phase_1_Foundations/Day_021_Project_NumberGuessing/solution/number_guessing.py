# Number Guessing Game — Day 21 Solution

import random

playing = True
while playing:
    secret = random.randint(1, 100)
    attempts = 0

    guess = int(input("Guess a number between 1 and 100: "))

    while guess != secret:
        attempts += 1
        if guess > secret:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        guess = int(input("Guess again: "))

    attempts += 1
    print(f"Correct! The number was {secret}. You got it in {attempts} guess(es).")

    again = input("\nPlay again? (yes/no): ").lower().strip()
    playing = (again == "yes")

print("Thanks for playing!")
