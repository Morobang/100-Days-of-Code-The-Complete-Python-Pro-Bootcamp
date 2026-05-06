# Day 37 — Quick Reference: Parameters and Arguments

## Syntax
```python
def function_name(param1, param2):
    # use param1 and param2 as local variables
    ...

function_name(arg1, arg2)   # call with arguments
```

## Terminology
| Term | Where | Example |
|------|-------|---------|
| **Parameter** | `def` line | `def greet(name):` → `name` is the parameter |
| **Argument** | Call | `greet('Alice')` → `'Alice'` is the argument |

## Positional arguments — order matters
```python
def describe(first, last, age):
    ...

describe('Alice', 'Smith', 30)   # first='Alice', last='Smith', age=30
describe(30, 'Alice', 'Smith')   # wrong order = wrong result!
```

## Any type can be an argument
```python
def show(x):
    print(x)

show(42)             # int
show('hello')        # str
show([1, 2, 3])      # list
show({'a': 1})       # dict
```

## Passing collections
```python
def print_items(items):
    for i, item in enumerate(items, 1):
        print(f'{i}. {item}')

print_items(['apple', 'banana'])
```

## Parameters are local
```python
x = 10

def change(x):
    x = 99    # local only — outer x unchanged

change(x)
print(x)    # still 10
```
