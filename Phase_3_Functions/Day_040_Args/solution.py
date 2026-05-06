# Day 40 Solutions

# Challenge 1
def my_sum(*args):
    result = 0
    for n in args:
        result += n
    return result

def my_product(*args):
    if not args:
        return 0
    result = 1
    for n in args:
        result *= n
    return result

print(my_sum())           # 0
print(my_sum(5))          # 5
print(my_sum(1, 2, 3, 4)) # 10
print(my_product())       # 0
print(my_product(3))      # 3
print(my_product(2, 3, 4))# 24

# Challenge 2
def print_all(label, *items):
    print(f'{label}:')
    for item in items:
        print(f'  - {item}')

print_all('Fruits', 'apple', 'banana', 'cherry')
print_all('Languages', 'Python', 'JavaScript', 'Go', 'Rust')
print_all('Empty list')

# Challenge 3
def stats(*numbers):
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = stats(10, 5, 88, 42, 7)
print(f'Min: {lo} | Max: {hi} | Avg: {avg:.2f}')

lo, hi, avg = stats()
print(lo, hi, avg)

scores = [88, 75, 92, 61, 79]
lo, hi, avg = stats(*scores)
print(f'Min: {lo} | Max: {hi} | Avg: {avg:.2f}')

# Challenge 4
def concatenate(separator, *words):
    if not words:
        return ''
    result = words[0]
    for word in words[1:]:
        result += separator + word
    return result

print(concatenate('-', 'hello', 'world'))
print(concatenate(', ', 'one', 'two', 'three'))
print(concatenate(' | ', 'a'))
print(concatenate('/', 'usr', 'local', 'bin'))

# Challenge 5
def apply_all(value, *functions):
    result = value
    for func in functions:
        result = func(result)
    return result

def double(x): return x * 2
def add_ten(x): return x + 10
def square(x): return x ** 2
def negate(x): return -x

print(apply_all(3, double, add_ten, square))  # 256
print(apply_all(5, square, negate))           # -25
print(apply_all(10, double, double, double))  # 80
