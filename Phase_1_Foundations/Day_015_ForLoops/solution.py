# Day 15 — Solutions

# Challenge 1: Print each character of a word
word = input("Enter a word: ")
for char in word:
    print(char)

# Challenge 2: Print 1 to 10 using range()
for i in range(1, 11):
    print(i)

# Challenge 3: Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Challenge 4: Count vowels
word = input("Enter a word: ")
count = 0
for char in word.lower():
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(f"Vowels found: {count}")

# Challenge 5: FizzBuzz 1–20
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
