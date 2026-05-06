# Day 39 Solutions

# Challenge 1
def greet(name, greeting='Hello', punctuation='!'):
    print(f'{greeting}, {name}{punctuation}')

greet('Alice')
greet('Bob', 'Good morning')
greet('Charlie', 'Hey', '.')
greet('Diana', punctuation='?')

# Challenge 2
def make_box(text, width=40, border_char='*'):
    border = border_char * width
    inner = f'{border_char}{text.center(width - 2)}{border_char}'
    print(border)
    print(inner)
    print(border)

make_box('Hello World!')
print()
make_box('Python', width=30)
print()
make_box('Settings', border_char='-')

# Challenge 3
def power(base, exponent=2):
    return base ** exponent

def power_table(base, max_exp=5):
    for exp in range(1, max_exp + 1):
        print(f'{base}^{exp} = {power(base, exp)}')

power_table(3)
print()
power_table(2, max_exp=8)

# Challenge 4
def search(items, target, case_sensitive=False):
    for item in items:
        if case_sensitive:
            if item == target:
                return True
        else:
            if item.lower() == target.lower():
                return True
    return False

words = ['Python', 'Java', 'Rust', 'Go']
print(search(words, 'python'))          # True
print(search(words, 'python', True))    # False
print(search(words, 'Python', True))    # True
print(search(words, 'ruby'))            # False

# Challenge 5
def format_table(data, headers=None, col_width=12):
    if headers:
        header_row = ''.join(str(h).ljust(col_width) for h in headers)
        print(header_row)
        print(('-' * col_width + ' ') * len(headers))
    for row in data:
        print(''.join(str(cell).ljust(col_width) for cell in row))

rows = [('Alice', 88, 'A'), ('Bob', 75, 'B'), ('Charlie', 92, 'A')]
format_table(rows, headers=('Name', 'Score', 'Grade'))
print()
format_table(rows, col_width=15)
