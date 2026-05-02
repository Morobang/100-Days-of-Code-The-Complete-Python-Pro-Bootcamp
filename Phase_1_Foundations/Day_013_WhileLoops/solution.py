# Day 13 — Solutions

# Challenge 1: Count from 1 to 5
n = 1
while n <= 5:
    print(n)
    n += 1

# Challenge 2: Countdown from 10 to 1, then "Blast off!"
n = 10
while n >= 1:
    print(n)
    n -= 1
print("Blast off!")

# Challenge 3: Print numbers until user enters 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    print(f"You entered: {number}")
    number = int(input("Enter a number (0 to stop): "))
print("Done.")

# Challenge 4: Input validation — keep asking until age is valid
age = int(input("Enter your age: "))
while age <= 0 or age > 120:
    print("That doesn't look like a valid age. Try again.")
    age = int(input("Enter your age: "))
print(f"Got it — you are {age} years old.")

# Challenge 5: Running total and count
total = 0
count = 0
number = float(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    count += 1
    number = float(input("Enter a number (0 to stop): "))
print(f"Numbers entered: {count}")
print(f"Total: {total}")
