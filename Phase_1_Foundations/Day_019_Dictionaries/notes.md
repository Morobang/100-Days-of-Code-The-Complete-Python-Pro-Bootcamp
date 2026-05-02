# Day 19 — Quick Reference

## Creating a dictionary

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Cape Town'}
empty = {}
```

## Accessing values

```python
person['name']    # 'Alice'  — KeyError if key doesn't exist
```

## Adding and updating

```python
person['email'] = 'alice@example.com'    # new key
person['age'] = 31                        # update existing key
```

## Deleting

```python
del person['email']    # removes the key — KeyError if missing
```

## Checking for a key

```python
'name' in person       # True
'phone' in person      # False
'phone' not in person  # True
```

## Iterating

```python
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:              # iterates over keys
    print(key)

for key in d.keys():       # same as above, explicit
    print(key)

for value in d.values():   # iterates over values
    print(value)

for key, value in d.items():   # key AND value together
    print(key, value)
```

## Building a dict with a loop

```python
frequency = {}
for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
```

## Gotchas

- Keys must be **unique** — setting the same key twice keeps the second value.
- Keys must be **immutable** — strings, numbers, and tuples are fine; lists are not.
- Accessing a missing key raises `KeyError`. Use `.get()` (Day 20) to avoid this.
- Dicts preserve insertion order (Python 3.7+).
