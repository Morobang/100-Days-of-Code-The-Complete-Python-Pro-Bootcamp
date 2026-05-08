# Day 44 Solutions

# Challenge 1
def outer():
    message = 'I am from the outer function'

    def inner():
        print(message)

    inner()

outer()

print()

# Challenge 2
def make_greeter(greeting):
    def greet(name):
        print(f'{greeting}, {name}!')
    return greet

hello = make_greeter('Hello')
hi = make_greeter('Hi')

hello('Alice')
hi('Bob')
hello('Charlie')

print()

# Challenge 3
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

print()

# Challenge 4
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)

print(square(4))   # 16
print(cube(3))     # 27
print(square(10))  # 100

print()

# Challenge 5
def make_pipeline(func1, func2):
    def pipeline(value):
        return func2(func1(value))
    return pipeline

def double(x):
    return x * 2

def add_ten(x):
    return x + 10

double_then_add = make_pipeline(double, add_ten)
add_then_double = make_pipeline(add_ten, double)

print(double_then_add(5))  # (5 * 2) + 10 = 20
print(add_then_double(5))  # (5 + 10) * 2 = 30
