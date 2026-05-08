# Day 53 Solutions

# Challenge 1
def get_positive(n):
    if n <= 0:
        raise ValueError(f'{n} is not positive')
    return n

for val in [5, -3, 0]:
    try:
        print(get_positive(val))
    except ValueError as e:
        print(f'Error: {e}')

print()

# Challenge 2
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('cannot divide by zero')
    return a / b

for pair in [(10, 2), (10, 0)]:
    try:
        print(divide(*pair))
    except ZeroDivisionError as e:
        print(f'Error: {e}')

print()

# Challenge 3
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f'age must be an int, got {type(age).__name__}')
    if age < 0 or age > 150:
        raise ValueError(f'age must be 0–150, got {age}')
    return age

for val in [25, -1, 200, 'thirty']:
    try:
        print(validate_age(val))
    except (ValueError, TypeError) as e:
        print(f'Error: {e}')

print()

# Challenge 4
def safe_open(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Required file '{filename}' is missing")

try:
    safe_open('ghost.txt')
except FileNotFoundError as e:
    print(f'Error: {e}')

print()

# Challenge 5
def risky():
    raise RuntimeError('something went wrong')

def wrapper():
    try:
        risky()
    except RuntimeError:
        print('wrapper: caught, logging, re-raising')
        raise

try:
    wrapper()
except RuntimeError as e:
    print(f'outer: {e}')
