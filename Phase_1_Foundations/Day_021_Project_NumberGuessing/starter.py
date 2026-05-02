# Number Guessing Game — Day 21 Project
# ----------------------------------------
# New concept today:
#   import random             — loads Python's random module
#   random.randint(1, 100)    — random integer between 1 and 100 (inclusive)

import random

# Outer loop — lets the player start a new game
playing = True
while playing:

    # Step 1: Pick the secret number (already done for you!)
    secret = random.randint(1, 100)

    # Step 2: Set up an attempt counter
    attempts = ...

    # Step 3: Get the first guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Step 4: Keep looping while the guess is wrong
    while ...:

        # Step 4a: Increment the attempt counter
        ...

        # Step 4b: Give a hint — too high or too low?
        if ...:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        # Step 4c: Get the next guess
        guess = int(input("Guess again: "))

    # Step 5: Count the final (correct) attempt and congratulate
    ...
    print(f"Correct! The number was {secret}. You got it in {attempts} guess(es).")

    # Step 6: Ask to play again
    again = input("\nPlay again? (yes/no): ").lower().strip()
    playing = (again == "yes")

print("Thanks for playing!")
