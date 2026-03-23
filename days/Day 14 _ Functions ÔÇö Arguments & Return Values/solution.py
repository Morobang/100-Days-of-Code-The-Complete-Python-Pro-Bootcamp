# Day 14 — Functions: Arguments & Return Values — SOLUTIONS

# Exercise 1
def describe_player(*games, **stats):
    print("Games:", list(games))
    for key, val in stats.items():
        print(f"{key}: {val}")


# Exercise 2
def calculator(a, b, operation='add'):
    if operation == 'add':      return a + b
    if operation == 'subtract': return a - b
    if operation == 'multiply': return a * b
    if operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError(f"Unknown operation: {operation}")


# Exercise 3 — closure
def make_multiplier(factor):
    # inner function 'remembers' factor from the enclosing scope
    def multiply(x):
        return x * factor
    return multiply
