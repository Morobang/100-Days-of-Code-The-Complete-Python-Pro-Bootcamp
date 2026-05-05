# Day 30 Solutions

# Challenge 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2]
unique = set(numbers)
print('Unique:', unique)
print('Count:', len(unique))
print('Sorted:', sorted(unique))
print('Duplicates removed:', len(numbers) - len(unique))

# Challenge 2
team_a = {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
team_b = {'Charlie', 'Diana', 'Frank', 'Grace', 'Eve'}
print('In both:',        sorted(team_a & team_b))
print('All players:',    sorted(team_a | team_b))
print('Only in A:',      sorted(team_a - team_b))
print('Only in B:',      sorted(team_b - team_a))
print('Exactly one:',    sorted(team_a ^ team_b))

# Challenge 3
required = {'python', 'sql', 'excel', 'statistics'}
candidates = {
    'Candidate A': {'python', 'sql', 'excel', 'statistics', 'r'},
    'Candidate B': {'python', 'excel', 'tableau'},
    'Candidate C': {'sql', 'statistics', 'excel', 'python'}
}
for name, skills in candidates.items():
    has = skills & required
    missing = required - skills
    qualified = required.issubset(skills)
    print(f'{name}:')
    print(f'  Has: {sorted(has)}')
    print(f'  Missing: {sorted(missing)}')
    print(f'  Meets all requirements: {qualified}')

# Challenge 4
line1 = input('First set of words: ')
line2 = input('Second set of words: ')
set1 = set(line1.lower().split())
set2 = set(line2.lower().split())
print('Common:', sorted(set1 & set2))
print('Combined:', sorted(set1 | set2))
print('Only in first:', sorted(set1 - set2))
print('Only in second:', sorted(set2 - set1))
print('No words in common:', set1.isdisjoint(set2))

# Challenge 5
articles = {
    'Python Basics':       {'python', 'beginner', 'programming'},
    'Data with Pandas':    {'python', 'data', 'pandas'},
    'SQL Intro':           {'sql', 'data', 'beginner'},
    'Machine Learning 101':{'python', 'data', 'ml', 'beginner'},
    'Advanced SQL':        {'sql', 'data', 'advanced'}
}

tag1 = input('Search tag: ').lower()
matches1 = []
for title, tags in articles.items():
    if tag1 in tags:
        matches1.append(title)
print('Found:', ', '.join(matches1) if matches1 else 'None')

tag2 = input('Second tag: ').lower()
matches2 = []
for title, tags in articles.items():
    if tag1 in tags and tag2 in tags:
        matches2.append(title)
print('Both tags:', ', '.join(matches2) if matches2 else 'None')
