# Day 29 Solutions

# Challenge 1
library = {
    'Python Crash Course': {'author': 'Matthes', 'year': 2019, 'available': True},
    'Clean Code':          {'author': 'Martin',  'year': 2008, 'available': False},
    'The Pragmatic Programmer': {'author': 'Thomas', 'year': 2019, 'available': True}
}
print(library['Clean Code']['author'])
print(library['Python Crash Course']['year'])
print(library['The Pragmatic Programmer']['available'])
print(library.get('SICP', 'Not in library'))

# Challenge 2
library['Clean Code']['available'] = True
library['Python Crash Course']['pages'] = 544
library['Fluent Python'] = {'author': 'Ramalho', 'year': 2022, 'available': True}
for title, info in library.items():
    print(f'{title}: {info}')

# Challenge 3
products = {
    'laptop':  {'price': 12000, 'stock': 5,  'category': 'electronics'},
    'mouse':   {'price': 350,   'stock': 20, 'category': 'electronics'},
    'desk':    {'price': 4500,  'stock': 3,  'category': 'furniture'},
    'chair':   {'price': 3200,  'stock': 8,  'category': 'furniture'},
    'monitor': {'price': 6800,  'stock': 7,  'category': 'electronics'}
}

print('Electronics:')
for name, info in products.items():
    if info['category'] == 'electronics':
        print(f'  {name}: R{info["price"]}')

total_value = 0
for info in products.values():
    total_value += info['price'] * info['stock']
print(f'Total stock value: R{total_value}')

priciest = None
priciest_val = -1
for name, info in products.items():
    if info['price'] > priciest_val:
        priciest_val = info['price']
        priciest = name
print('Most expensive:', priciest)

# Challenge 4
team = {
    'Alice':   {'tasks_done': 12, 'tasks_total': 15},
    'Bob':     {'tasks_done': 8,  'tasks_total': 10},
    'Charlie': {'tasks_done': 5,  'tasks_total': 20},
    'Diana':   {'tasks_done': 18, 'tasks_total': 18}
}
for info in team.values():
    info['pct'] = round(info['tasks_done'] / info['tasks_total'] * 100, 1)

ranked = []
for name, info in team.items():
    ranked.append((info['pct'], name))
ranked.sort(reverse=True)

for pct, name in ranked:
    print(f'{name}: {pct}%')

# Challenge 5
students = {}
while True:
    name = input("Name (or 'done'): ").strip()
    if name == 'done':
        break
    age = int(input('Age: '))
    score = int(input('Score: '))
    students[name] = {'age': age, 'score': score}

if students:
    for name, info in students.items():
        s = info['score']
        if s >= 80:
            grade = 'A'
        elif s >= 70:
            grade = 'B'
        elif s >= 60:
            grade = 'C'
        elif s >= 50:
            grade = 'D'
        else:
            grade = 'F'
        info['grade'] = grade
        print(f"{name:10} | age {info['age']} | score {s} | grade {grade}")

    top = None
    top_score = -1
    for name, info in students.items():
        if info['score'] > top_score:
            top_score = info['score']
            top = name
    total = 0
    for info in students.values():
        total += info['score']
    avg = total / len(students)
    print(f'Top: {top} ({top_score})')
    print(f'Average: {avg:.1f}')
