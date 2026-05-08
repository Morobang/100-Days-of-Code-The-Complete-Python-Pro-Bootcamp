# Day 50 Solutions

# Challenge 1
with open('greeting.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, file world!\n')

with open('greeting.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Challenge 2
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
with open('fruits.txt', 'w', encoding='utf-8') as f:
    for fruit in fruits:
        f.write(fruit + '\n')

with open('fruits.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Challenge 3
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('First entry\n')

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Second entry\n')

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Third entry\n')

with open('log.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Challenge 4
lines = ['line one\n', 'line two\n', 'line three\n']
with open('writelines_demo.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open('writelines_demo.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Challenge 5
with open('numbers.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 11):
        f.write(str(i) + '\n')

total = 0
with open('numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        total += int(line.strip())
print(f'Sum: {total}')  # 55
