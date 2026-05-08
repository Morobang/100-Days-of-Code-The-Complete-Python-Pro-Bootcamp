# Day 52 Solutions

# Challenge 1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error: cannot divide by zero')
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error message, then None

print()

# Challenge 2
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        print(f"'{s}' is not a valid integer")
        return None

print(safe_int('42'))    # 42
print(safe_int('abc'))   # error message, then None
print(safe_int('3.5'))   # error message, then None

print()

# Challenge 3
def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None

print(read_file_safe('nope.txt'))

print()

# Challenge 4
def parse_number(s):
    try:
        value = int(s)
    except ValueError:
        print(f"ValueError: '{s}' is not an integer")
        return None
    except TypeError:
        print(f'TypeError: expected a string, got {type(s).__name__}')
        return None
    else:
        print(f'Parsed successfully: {value}')
        return value

parse_number('10')
parse_number('abc')
parse_number(None)

print()

# Challenge 5
def safe_divide_finally(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: division by zero')
        result = None
    else:
        print(f'Result: {result}')
    finally:
        print('safe_divide_finally complete')
    return result

safe_divide_finally(10, 2)
print()
safe_divide_finally(10, 0)
