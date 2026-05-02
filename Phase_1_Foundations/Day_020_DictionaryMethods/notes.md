# Day 20 — Quick Reference

## .get() — safe lookup

```python
d = {'a': 1, 'b': 2}
d.get('a')          # 1
d.get('z')          # None  — no KeyError
d.get('z', 0)       # 0     — custom default
```

## .keys(), .values(), .items()

```python
d = {'name': 'Alice', 'age': 30}
list(d.keys())      # ['name', 'age']
list(d.values())    # ['Alice', 30]
list(d.items())     # [('name', 'Alice'), ('age', 30)]

for key, value in d.items():
    print(key, value)
```

## .update() — merge / bulk update

```python
d = {'a': 1, 'b': 2}
d.update({'b': 99, 'c': 3})
print(d)    # {'a': 1, 'b': 99, 'c': 3}
# existing keys are overwritten, new keys are added
```

## .pop() — remove and return

```python
d = {'a': 1, 'b': 2}
val = d.pop('a')      # removes 'a' and returns 1
print(val)            # 1
print(d)              # {'b': 2}
d.pop('z', None)      # safe pop with a default — no KeyError
```

## .setdefault() — set only if missing

```python
d = {'a': 1}
d.setdefault('b', 0)   # adds 'b': 0 because 'b' is missing
d.setdefault('a', 99)  # does nothing — 'a' already exists
print(d)               # {'a': 1, 'b': 0}
```

## Nested dictionaries

```python
students = {
    'Alice': {'score': 88, 'grade': 'B'},
    'Bob':   {'score': 75, 'grade': 'C'},
}
print(students['Alice']['score'])   # 88
students['Alice']['score'] = 90
```

## Gotchas

- `.get()` returns `None` by default, not an error — check the return value if `None` is meaningful.
- `.update()` **overwrites** existing keys with the new values.
- `.pop()` raises KeyError if the key is missing and no default is given.
