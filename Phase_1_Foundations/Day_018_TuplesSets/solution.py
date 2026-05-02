# Day 18 — Solutions

# Challenge 1: Tuple indexing
person = ("Alice", 30, "Cape Town")
print("Name:", person[0])
print("Age: ", person[1])
print("City:", person[2])

# Challenge 2: Tuple unpacking
name, age, city = person
print(f"{name} is {age} years old and lives in {city}.")

# Challenge 3: Remove duplicates with a set
numbers = [1, 3, 2, 1, 5, 3, 2, 4, 1, 5]
unique = set(numbers)
print("Unique values:", unique)
print("Count:", len(unique))

# Challenge 4: Set operations
class_a = {"Alice", "Bob", "Charlie", "Diana"}
class_b = {"Charlie", "Diana", "Eve", "Frank"}
print("In both:      ", class_a & class_b)
print("In either:    ", class_a | class_b)
print("Only in A:    ", class_a - class_b)
print("Only in B:    ", class_b - class_a)

# Challenge 5: Unique number tracker
seen = set()
for i in range(10):
    n = int(input(f"Enter number {i + 1}: "))
    seen.add(n)
print(f"You entered {len(seen)} unique value(s): {sorted(seen)}")
