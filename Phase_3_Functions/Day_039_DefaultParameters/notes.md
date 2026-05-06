# Day 39 — Quick Reference: Default Parameters

## Syntax
```python
def func(required, optional='default'):
    ...
```

## Rules
- Required parameters first, defaults after
- `def f(x=1, y):` → SyntaxError (required after default)
- Caller can override any default by passing a value
- Caller can use keyword arguments to skip middle params

## Calling patterns
```python
def connect(host, port=5432, timeout=30):
    ...

connect('db')                   # port=5432, timeout=30
connect('db', 3306)             # timeout=30
connect('db', 3306, 10)         # all supplied
connect('db', timeout=5)        # skip port, set timeout by name
connect(timeout=60, host='x')   # all by name, any order
```

## The mutable default trap
```python
# WRONG — list is shared across all calls
def bad(items=[]):
    items.append(1)
    return items

# CORRECT — use None, create inside
def good(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

## Common use cases
```python
def greet(name, greeting='Hello'):          # optional greeting
def print_items(items, numbered=True):      # toggle numbering
def connect(host, port=5432, timeout=30):   # sensible defaults
def make_header(text, width=40, char='='):  # formatting options
```
