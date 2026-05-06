# Day 40 — Quick Reference: *args

## Syntax
```python
def func(*args):
    # args is a tuple
    for item in args:
        print(item)
```

## Key facts
- `args` is a **tuple** inside the function
- Can be called with zero or more positional arguments
- Name `args` is convention — `*numbers`, `*items` also work
- Must come after regular parameters

## Ordering rules
```python
def func(required, *args):          # regular → *args
    ...

def func(req, *args, kw_only=val):  # after *args = keyword-only
    ...
```

## Iterating
```python
def total(*args):
    result = 0
    for n in args:
        result += n
    return result
```

## Guard for empty args
```python
def first(*args):
    if not args:
        return None
    return args[0]
```

## Unpacking at the call site
```python
numbers = [1, 2, 3]
func(*numbers)       # same as func(1, 2, 3)
func(*range(1, 6))   # func(1, 2, 3, 4, 5)
```

## Combined example
```python
def log(level, *messages):
    for msg in messages:
        print(f'[{level}] {msg}')

log('INFO', 'Server started', 'Listening on 8080')
```
