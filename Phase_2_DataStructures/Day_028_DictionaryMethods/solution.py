# Day 28 Solutions

# Challenge 1
book1 = {'title': '1984', 'author': 'Orwell', 'year': 1949}
book2 = dict(title='1984', author='Orwell', year=1949)
book3 = dict([('title', '1984'), ('author', 'Orwell'), ('year', 1949)])
print(book1)
print(book2)
print(book3)
print(book1 == book2 == book3)  # True

# Challenge 2
items = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
stock = dict.fromkeys(items, 0)
stock['apple'] = 50
stock['banana'] = 30
stock['kiwi'] = 15
print(stock)

# Challenge 3
base     = {'host': 'localhost', 'port': 5432, 'db': 'myapp', 'debug': False}
override = {'port': 3306, 'debug': True}
merged = {**base, **override, 'version': '2.0'}
print(merged)
print('base unchanged:', base)
print('override unchanged:', override)

# Challenge 4
session = {'user': 'Alice', 'token': 'xyz999', 'role': 'admin', 'temp_flag': True}
token = session.pop('token')
print('Removed token:', token)
expires = session.pop('expires_at', 'not set')
print('expires_at:', expires)
print(session)

# Challenge 5
freq = {}
total = 0
while True:
    item = input('Item: ').strip()
    if item == 'done':
        break
    freq[item] = freq.get(item, 0) + 1
    total += 1

if freq:
    for key in sorted(freq):
        print(f'{key}: {freq[key]}')
    print('Most common:', max(freq, key=freq.get))
    print('Least common:', min(freq, key=freq.get))
    print('Total entries:', total)
else:
    print('No items entered.')
