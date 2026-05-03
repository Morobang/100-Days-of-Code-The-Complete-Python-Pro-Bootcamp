# Day 27 Solutions

# Challenge 1
results = ['pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'fail', 'pass']
counts = {}
for r in results:
    counts[r] = counts.get(r, 0) + 1
for result, count in counts.items():
    print(f'{result}: {count}')

# Challenge 2
sentence = input('Enter a sentence: ').lower()
freq = {}
for char in sentence:
    if char != ' ':
        freq[char] = freq.get(char, 0) + 1
for letter in sorted(freq):
    print(f'{letter}: {freq[letter]}')

# Challenge 3
students = [
    ('Alice', 'Maths'),
    ('Bob', 'Science'),
    ('Charlie', 'Maths'),
    ('Diana', 'English'),
    ('Eve', 'Science'),
    ('Frank', 'Maths')
]
groups = {}
for name, subject in students:
    groups.setdefault(subject, []).append(name)
print(groups)

# Challenge 4
elements = ['Hydrogen', 'Helium', 'Lithium', 'Carbon', 'Oxygen']
symbols  = ['H', 'He', 'Li', 'C', 'O']

name_to_symbol = {}
for i in range(len(elements)):
    name_to_symbol[elements[i]] = symbols[i]

symbol_to_name = {}
for name, symbol in name_to_symbol.items():
    symbol_to_name[symbol] = name

query = input('Enter element or symbol: ').strip()
if query in name_to_symbol:
    print(f'{query} → {name_to_symbol[query]}')
elif query in symbol_to_name:
    print(f'{query} → {symbol_to_name[query]}')
else:
    print('Not found.')

# Challenge 5
scores = {}
while True:
    name = input("Name (or 'done'): ").strip()
    if name == 'done':
        break
    score = int(input('Score: '))
    scores[name] = score

if not scores:
    print('No scores entered.')
else:
    grade_counts = {}
    for score in scores.values():
        if score >= 80:
            grade = 'A'
        elif score >= 70:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        elif score >= 50:
            grade = 'D'
        else:
            grade = 'F'
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    print('\nGrade distribution:')
    for grade in ['A', 'B', 'C', 'D', 'F']:
        if grade in grade_counts:
            print(f'  {grade}: {grade_counts[grade]}')

    top = max(scores, key=scores.get)
    print(f'Top scorer: {top} — {scores[top]}')
    avg = sum(scores.values()) / len(scores)
    print(f'Average: {round(avg, 1)}')
