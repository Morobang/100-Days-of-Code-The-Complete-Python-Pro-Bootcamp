# Day 47 Solutions

# Challenge 1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

print()

# Challenge 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]

print()

# Challenge 3
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16, 25]

print()

# Challenge 4
numbers = range(1, 11)
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16, 36, 64, 100]

print()

# Challenge 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

via_map_filter = list(map(lambda x: x * 3, filter(lambda x: x % 2 != 0, numbers)))
via_comprehension = [x * 3 for x in numbers if x % 2 != 0]

print(via_map_filter)                           # [3, 9, 15, 21, 27]
print(via_comprehension)                        # [3, 9, 15, 21, 27]
print(via_map_filter == via_comprehension)      # True
