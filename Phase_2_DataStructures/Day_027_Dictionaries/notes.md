# Day 27 — Quick Reference: Dictionary Patterns

## Counting occurrences
```python
counts = {}
for item in sequence:
    counts[item] = counts.get(item, 0) + 1
```

## Grouping items (values as lists)
```python
groups = {}
for item in sequence:
    key = item[0]                          # or whatever determines the group
    groups.setdefault(key, []).append(item)
```

## Building a dict from two parallel lists
```python
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
```

## Inverting a dictionary
```python
inverted = {}
for k, v in original.items():
    inverted[v] = k
```

## Sorting by key
```python
for k, v in sorted(d.items()):
    print(k, v)
```

## Sorting by value
```python
pairs = []
for k, v in d.items():
    pairs.append((v, k))
pairs.sort(reverse=True)   # highest value first
for v, k in pairs:
    print(k, v)
```

## Finding max/min value
```python
max(d, key=d.get)   # key with highest value
min(d, key=d.get)   # key with lowest value
```
