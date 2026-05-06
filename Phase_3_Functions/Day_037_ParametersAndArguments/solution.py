# Day 37 Solutions

# Challenge 1
def greet(name):
    print(f'Hello, {name}! Welcome.')

greet('Alice')
greet('Bob')
greet('Charlie')
greet('Diana')

# Challenge 2
def describe_book(title, author, year):
    print(f"'{title}' by {author} ({year})")

describe_book('1984', 'George Orwell', 1949)
describe_book('Clean Code', 'Robert Martin', 2008)
describe_book('Python Crash Course', 'Eric Matthes', 2019)

# Challenge 3
def print_list(title, items):
    print(title)
    print('-' * len(title))
    for i, item in enumerate(items, 1):
        print(f'  {i}. {item}')

print_list('Shopping List', ['milk', 'eggs', 'bread', 'butter'])
print()
print_list('To-Do Today', ['study Python', 'exercise', 'read'])

# Challenge 4
def print_score_report(name, score, subject):
    if score >= 80:   grade = 'A'
    elif score >= 70: grade = 'B'
    elif score >= 60: grade = 'C'
    elif score >= 50: grade = 'D'
    else:             grade = 'F'
    print(f'{name:<10} | {subject:<10} | Score: {score} | Grade: {grade}')

print_score_report('Alice',   88, 'Maths')
print_score_report('Bob',     45, 'Science')
print_score_report('Charlie', 72, 'English')
print_score_report('Diana',   91, 'Maths')

# Challenge 5
data = [('Alice', 88), ('Bob', 45), ('Charlie', 72),
        ('Diana', 91), ('Eve', 55), ('Frank', 78)]

def print_all_results(results):
    print('All results:')
    for name, score in results:
        print(f'  {name}: {score}')

def print_passing(results):
    print('Passing (≥70):')
    for name, score in results:
        if score >= 70:
            print(f'  {name}: {score}')

def print_failing(results):
    print('Failing (<70):')
    for name, score in results:
        if score < 70:
            print(f'  {name}: {score}')

def print_top_scorer(results):
    top_name, top_score = results[0]
    for name, score in results:
        if score > top_score:
            top_name, top_score = name, score
    print(f'Top scorer: {top_name} ({top_score})')

def print_summary(results):
    scores = [score for _, score in results]
    print(f'Count: {len(scores)}')
    print(f'Average: {sum(scores)/len(scores):.1f}')
    print(f'Highest: {max(scores)}')
    print(f'Lowest: {min(scores)}')

print_all_results(data)
print()
print_passing(data)
print()
print_failing(data)
print()
print_top_scorer(data)
print()
print_summary(data)
