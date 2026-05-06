# Day 38 — Quick Reference: Return Values

## Basic return
```python
def square(n):
    return n ** 2

result = square(5)    # result = 25
print(square(3))      # 9
print(square(4) + 1)  # 17 — use directly in an expression
```

## Return vs print
```python
def f_print(n): print(n * 2)   # shows output, returns None
def f_return(n): return n * 2  # produces a value, shows nothing

a = f_print(5)   # prints 10, a = None
b = f_return(5)  # b = 10, nothing printed
```

## Returning different types
```python
def is_even(n): return n % 2 == 0        # bool
def grade(s):   return 'A' if s>=80 else 'B'  # str
def doubled(lst): return [x*2 for x in lst]   # list
```

## Returning multiple values (tuple)
```python
def min_max(nums):
    return min(nums), max(nums)   # returns a tuple

lo, hi = min_max([3, 1, 8])      # unpack
result = min_max([3, 1, 8])      # result is (1, 8)
```

## Early return
```python
def safe_div(a, b):
    if b == 0:
        return None    # exits immediately
    return a / b
```

## No return → None
```python
def show():
    print('hi')

x = show()   # x is None
```

## Chaining calls
```python
print(f(g(x)))         # g runs first, result passed to f
a = g(x); b = f(a)    # same thing, step by step
```
