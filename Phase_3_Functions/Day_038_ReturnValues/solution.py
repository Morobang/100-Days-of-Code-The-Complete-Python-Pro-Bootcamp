# Day 38 Solutions

# Challenge 1
def cube(n):
    return n ** 3

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def initials(first, last):
    return f'{first[0].upper()}.{last[0].upper()}.'

print(cube(3))
print(cube(5))
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(initials('alice', 'smith'))
print(initials('Bob', 'Jones'))

# Challenge 2
def is_palindrome(word):
    return word == word[::-1]

def is_strong_password(password):
    if len(password) < 8:
        return False
    for ch in password:
        if ch.isdigit():
            return True
    return False

print(is_palindrome('racecar'))  # True
print(is_palindrome('hello'))    # False
print(is_palindrome('level'))    # True

print(is_strong_password('abc'))        # False — too short
print(is_strong_password('abcdefgh'))   # False — no digit
print(is_strong_password('abcde123'))   # True

# Challenge 3
def analyse(numbers):
    return min(numbers), max(numbers), sum(numbers), sum(numbers) / len(numbers)

lo, hi, total, avg = analyse([15, 3, 88, 42, 7, 61])
print(f'Min: {lo} | Max: {hi} | Total: {total} | Average: {avg:.2f}')

# Challenge 4
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

def format_result(result):
    if result is None:
        return 'Error: division by zero'
    return f'{result:.2f}'

print(format_result(safe_divide(10, 2)))   # 5.00
print(format_result(safe_divide(7, 3)))    # 2.33
print(format_result(safe_divide(5, 0)))    # Error: division by zero

# Challenge 5
def get_value(prompt):
    return float(input(prompt))

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def format_conversion(original, unit_from, result, unit_to):
    return f'{original} {unit_from} = {result:.2f} {unit_to}'

def run_converter():
    print('1. km → miles')
    print('2. miles → km')
    print('3. kg → pounds')
    choice = input('Choice: ')
    if choice == '1':
        val = get_value('km: ')
        print(format_conversion(val, 'km', km_to_miles(val), 'miles'))
    elif choice == '2':
        val = get_value('miles: ')
        print(format_conversion(val, 'miles', miles_to_km(val), 'km'))
    elif choice == '3':
        val = get_value('kg: ')
        print(format_conversion(val, 'kg', kg_to_pounds(val), 'pounds'))
    else:
        print('Invalid choice.')

run_converter()
