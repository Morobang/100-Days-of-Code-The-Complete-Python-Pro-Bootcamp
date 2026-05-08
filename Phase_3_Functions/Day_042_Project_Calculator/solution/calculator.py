# Day 42 Solution: Calculator

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print('Error: cannot divide by zero.')
        return None
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        print('Error: cannot modulo by zero.')
        return None
    return a % b

def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a valid number. Try again.")

def calculate(a, op, b):
    operations = {
        '+':  add,
        '-':  subtract,
        '*':  multiply,
        '/':  divide,
        '**': power,
        '%':  modulo,
    }
    if op not in operations:
        print(f"Unknown operator '{op}'.")
        return None
    return operations[op](a, b)

def format_result(a, op, b, result):
    if result is None:
        return f'{a} {op} {b} = ERROR'
    return f'{a} {op} {b} = {result}'

def show_history():
    if not history:
        print('No calculations yet.')
    else:
        for i, entry in enumerate(history, 1):
            print(f'{i}. {entry}')

print('=== Calculator ===')

while True:
    print('\n1. Calculate')
    print('2. Show history')
    print('3. Clear history')
    print('4. Quit')

    choice = input('Choice: ').strip()

    if choice == '1':
        a = get_number('First number: ')
        op = input('Operation (+, -, *, /, **, %): ').strip()
        b = get_number('Second number: ')
        result = calculate(a, op, b)
        entry = format_result(a, op, b, result)
        history.append(entry)
        print('Result:', entry)

    elif choice == '2':
        show_history()

    elif choice == '3':
        history.clear()
        print('History cleared.')

    elif choice == '4':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Enter 1–4.')
