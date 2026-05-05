# Day 28 — Quick Reference: Dictionary Methods

## Creating dicts
```python
d = {'a': 1}                     # literal
d = dict(a=1, b=2)               # keyword args
d = dict([('a', 1), ('b', 2)])   # from list of tuples
d = dict.fromkeys(keys, default) # all values = default
```

## Adding / updating
```python
d['key'] = value             # single key
d.update({'key': value})     # from dict
d.update(key=value)          # keyword args
d.update(other, key=value)   # both at once
```

## Reading safely
```python
d.get('key')           # None if missing
d.get('key', default)  # default if missing
```

## Removing
```python
d.pop('key')           # KeyError if missing
d.pop('key', default)  # returns default if missing
del d['key']           # KeyError if missing
d.clear()              # empty the dict
```

## Merging (creates new dict)
```python
merged = {**d1, **d2}              # d2 overwrites d1 on conflict
merged = {**d1, **d2, 'extra': 1}  # add extra keys inline
```

## Iterating
```python
d.keys()     # all keys
d.values()   # all values
d.items()    # all (key, value) pairs
sorted(d.items())  # sorted by key
```

## Finding min / max value
```python
max(d, key=d.get)   # key with highest value
min(d, key=d.get)   # key with lowest value
```
