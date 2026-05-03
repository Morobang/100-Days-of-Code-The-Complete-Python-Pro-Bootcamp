# Day 25 Solutions

# Challenge 1
colours = ('red', 'green', 'blue', 'red', 'yellow', 'blue', 'red')
print(colours.count('red'))
print(colours.index('blue'))
print(colours.index('blue', colours.index('blue') + 1))
print(len(colours))

# Challenge 2
temperatures = (22.5, 19.0, 25.3, 18.7, 23.1, 20.8)
print('Highest:', max(temperatures))
print('Lowest:', min(temperatures))
print('Sorted:', sorted(temperatures))
print('Average:', round(sum(temperatures) / len(temperatures), 1))

# Challenge 3
numbers = []
for i in range(5):
    n = float(input(f'Number {i+1}: '))
    numbers.append(n)
numbers_tuple = tuple(numbers)
print('Tuple:', numbers_tuple)
print('Largest:', max(numbers_tuple))
print('Smallest:', min(numbers_tuple))
print('7 in tuple:', 7 in numbers_tuple)

# Challenge 4
scoreboard = [('Alice', 88), ('Bob', 75), ('Charlie', 92), ('Diana', 75), ('Eve', 88)]

# Alphabetical
print('Alphabetical:', sorted(scoreboard))

# By score descending
flipped = []
for name, score in scoreboard:
    flipped.append((score, name))
flipped.sort(reverse=True)
print('By score (highest first):', flipped)

# Challenge 5
grid = {
    (0, 0): 'top-left',
    (0, 1): 'top-centre',
    (0, 2): 'top-right',
    (1, 0): 'middle-left',
    (1, 1): 'centre',
    (1, 2): 'middle-right',
    (2, 0): 'bottom-left',
    (2, 1): 'bottom-centre',
    (2, 2): 'bottom-right'
}

while True:
    row_input = input("Row (or 'quit'): ")
    if row_input == 'quit':
        break
    col_input = input('Column: ')
    key = (int(row_input), int(col_input))
    print(grid.get(key, 'Empty'))
