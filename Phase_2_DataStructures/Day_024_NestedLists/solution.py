# Day 24 Solutions

# Challenge 1
grid = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(grid[0][2])         # 30
print(grid[2][0])         # 70
print(grid[1][1])         # 50 — centre
print(grid[1])            # [40, 50, 60]
print(grid[-1][-1])       # 90

# Challenge 2
classroom = [
    ['Alice', 'Bob', 'Charlie'],
    ['Diana', 'Eve', 'Frank'],
    ['Grace', 'Heidi', 'Ivan']
]
for i, row in enumerate(classroom):
    print(f'Row {i+1}: {" | ".join(row)}')

# Challenge 3
numbers = [
    [3, 7, 2, 9],
    [1, 5, 8, 4],
    [6, 0, 3, 7]
]
largest = numbers[0][0]
total = 0
count_above_5 = 0

for row in numbers:
    for val in row:
        if val > largest:
            largest = val
        total += val
        if val > 5:
            count_above_5 += 1

print('Largest:', largest)
print('Sum:', total)
print('Values > 5:', count_above_5)

# Challenge 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = []
for row in matrix:
    for item in row:
        flat.append(item)
print(flat)
print('Sum:', sum(flat))
print('Min:', min(flat))
print('Max:', max(flat))

# Challenge 5
table = []
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    table.append(row)

for row in table:
    for val in row:
        print(f'{val:4}', end='')
    print()
