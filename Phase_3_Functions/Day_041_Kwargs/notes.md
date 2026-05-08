# Day 41 — Quick Reference: **kwargs

## Syntax
```python
def func(**kwargs):
    # kwargs is a dict
    for key, value in kwargs.items():
        print(key, value)
```

## Key facts
- `kwargs` is a **dict** inside the function
- Keys are the argument names (strings), values are what was passed
- Name `kwargs` is convention — `**options`, `**config` also work
- Must come last in parameter list

## Ordering rules
```python
def func(required, *args, **kwargs):    # full order
    ...

def func(host='localhost', **options):  # defaults + kwargs
    ...
```

## Iterating
```python
def show(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')
```

## Checking for a specific key
```python
def func(**kwargs):
    name = kwargs.get('name', 'unknown')
```

## Unpacking a dict at the call site
```python
config = {'host': 'db', 'port': 5432}
connect(**config)           # connect(host='db', port=5432)

merged = {**defaults, **overrides}
connect(**merged)
```

## All parameter types together
```python
def full(req, *args, **kwargs):
    print(req)          # regular
    print(args)         # tuple of extra positionals
    print(kwargs)       # dict of keyword extras
```
