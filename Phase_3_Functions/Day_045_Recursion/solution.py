# Day 45 Solutions

# Challenge 1
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

print()

# Challenge 2
def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([10]))             # 10
print(sum_list([]))               # 0

print()

# Challenge 3
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(0))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800

print()

# Challenge 4
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 10))  # 1024
print(power(3, 4))   # 81
print(power(5, 0))   # 1

print()

# Challenge 5
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string('hello'))   # olleh
print(reverse_string('Python'))  # nohtyP
print(reverse_string(''))        # (empty string)
print(reverse_string('a'))       # a
