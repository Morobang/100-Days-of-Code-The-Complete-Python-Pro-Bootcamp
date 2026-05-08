# Day 46 Solutions

# Challenge 1
double = lambda x: x * 2
print(double(5))   # 10
print(double(3))   # 6
print(double(0))   # 0

print()

# Challenge 2
words = ['banana', 'apple', 'cherry', 'date']
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['date', 'apple', 'banana', 'cherry']

print()

# Challenge 3
pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
by_second = sorted(pairs, key=lambda t: t[1])
print(by_second)  # [(1, 'a'), (2, 'b'), (3, 'c')]

print()

# Challenge 4
add = lambda x, y: x + y
print(add(3, 7))   # 10
print(add(10, 5))  # 15
print(add(0, 0))   # 0

print()

# Challenge 5
people = [
    {'name': 'Charlie', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 35},
]
by_age = sorted(people, key=lambda p: p['age'])
for person in by_age:
    print(f"{person['name']}: {person['age']}")
# Alice: 25
# Charlie: 30
# Bob: 35
