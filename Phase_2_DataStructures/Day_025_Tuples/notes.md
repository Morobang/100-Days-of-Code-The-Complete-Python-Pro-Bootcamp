# Day 25 — Quick Reference: Tuples

## Creating tuples
```python
t = (1, 2, 3)
single = (42,)      # comma required — (42) is just 42 in parentheses
empty = ()
packed = 1, 2, 3    # parentheses optional
```

## Tuple methods (only two)
```python
t.count(x)          # number of times x appears
t.index(x)          # position of first x
t.index(x, start)   # search from 'start' onwards
```

## Works like a list (read-only)
```python
t[0]        # first item
t[-1]       # last item
t[1:3]      # slicing
len(t)      # length
min(t)      # smallest
max(t)      # largest
sum(t)      # total
x in t      # membership
```

## Converting
```python
list(t)     # tuple → list (now mutable)
tuple(lst)  # list → tuple (now immutable)
```

## Unpacking
```python
x, y = (3, 7)
r, g, b = (255, 128, 0)
```

## As dict keys
```python
d = {(0, 0): 'origin', (1, 2): 'point'}
d[(0, 0)]   # 'origin'
```

## Sorting a list of tuples
```python
sorted(lst)               # by first element
sorted(lst, reverse=True) # descending

# Sort by second element: rebuild with (second, first) then sort
swapped = []
for a, b in lst:
    swapped.append((b, a))
swapped.sort()
```

## Tuple vs list
| Tuple | List |
|-------|------|
| Immutable | Mutable |
| Can be dict key | Cannot be dict key |
| `.count()` `.index()` only | Many methods |
| Use for fixed records | Use for collections that change |
