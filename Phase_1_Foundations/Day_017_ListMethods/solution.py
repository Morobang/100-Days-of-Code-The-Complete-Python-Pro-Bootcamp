# Day 17 — Solutions

# Challenge 1: Sort and reverse
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print("Sorted:  ", numbers)
numbers.reverse()
print("Reversed:", numbers)

# Challenge 2: count() and index()
items = ["apple", "banana", "apple", "cherry", "apple"]
print("Count of 'apple':", items.count("apple"))
print("First index of 'apple':", items.index("apple"))

# Challenge 3: Remove the largest
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i + 1}: "))
    numbers.append(n)
numbers.remove(max(numbers))
print("List after removing the largest:", numbers)

# Challenge 4: insert() at start, pop() from end
colours = ["red", "green", "blue"]
print("Before:", colours)
colours.insert(0, "purple")
colours.pop()
print("After: ", colours)

# Challenge 5: Full stats
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i + 1}: "))
    numbers.append(n)

total = sum(numbers)
average = total / len(numbers)
numbers.sort()

print(f"Sorted:  {numbers}")
print(f"Sum:     {total}")
print(f"Min:     {min(numbers)}")
print(f"Max:     {max(numbers)}")
print(f"Average: {average:.2f}")
