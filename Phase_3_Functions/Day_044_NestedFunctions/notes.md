# Nested Functions — Quick Reference

## Inner Functions
A function defined inside another function. Only callable from within the outer function.
```python
def outer():
    def inner():   # only visible inside outer
        print('inner')
    inner()
```

## Enclosing Scope (the E in LEGB)
The inner function can read variables from the outer function's scope — no keyword needed.
```python
def outer():
    x = 10

    def inner():
        print(x)   # reads enclosing scope — allowed

    inner()
```

## Closures
When an inner function is **returned**, it carries its enclosing scope with it.
The returned function "remembers" the variables from when it was created.
```python
def make_greeter(greeting):
    def greet(name):
        print(f'{greeting}, {name}!')  # greeting remembered after make_greeter returns
    return greet

hello = make_greeter('Hello')
hello('Alice')   # Hello, Alice!
```

## Factory Functions
A function that creates and returns another function, configured by its arguments.
```python
def make_multiplier(n):
    def multiply(x):
        return x * n   # n is captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

## `nonlocal` Keyword
Like `global` but for the **enclosing** scope.
Required when you want to *reassign* a variable from an outer (non-global) function.
```python
def make_counter():
    count = 0

    def increment():
        nonlocal count   # modify the enclosing count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
```

## Cheat Sheet: Keyword by Scope
| Goal | Keyword |
|------|---------|
| Reassign a **global** variable inside a function | `global` |
| Reassign an **enclosing** variable inside a nested function | `nonlocal` |
| Read either — no reassignment | *(no keyword needed)* |
