# Day 16 — Solutions

# Challenge 1: Favourite foods list
foods = ["pizza", "sushi", "tacos", "pasta", "ice cream"]
print("First:", foods[0])
print("Last: ", foods[-1])

# Challenge 2: Build a list from user input
names = []
for i in range(3):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)
print(names)
print(f"Total names: {len(names)}")

# Challenge 3: Print numbers greater than 10
numbers = [5, 12, 3, 18, 7, 25, 9, 11]
for num in numbers:
    if num > 10:
        print(num)

# Challenge 4: Search in a list
fruits = ["apple", "banana", "cherry", "mango", "grape"]
word = input("Enter a fruit to search for: ").lower()
if word in fruits:
    print(f"'{word}' is in the list!")
else:
    print(f"'{word}' is not in the list.")

# Challenge 5: Find the largest without max()
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i + 1}: "))
    numbers.append(n)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number is {largest}")
