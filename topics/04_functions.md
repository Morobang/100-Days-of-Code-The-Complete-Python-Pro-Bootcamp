# Functions

## Basics
```python
def greet(name):
    return f"Hello {name}"
```

## Default arguments
```python
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"
```

## *args and **kwargs
```python
def total(*args):           # args is a tuple
    return sum(args)

def display(**kwargs):      # kwargs is a dict
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

## Multiple returns
```python
def min_max(lst):
    return min(lst), max(lst)   # returns tuple

lo, hi = min_max([3,1,4,1,5])
```

## Scope
```python
x = 10              # global

def foo():
    global x        # modify global
    x = 99

def outer():
    count = 0
    def inner():
        nonlocal count  # modify enclosing scope
        count += 1
    inner()
    return count
```

## Lambda
```python
square = lambda x: x**2
names.sort(key=lambda n: len(n))
```
