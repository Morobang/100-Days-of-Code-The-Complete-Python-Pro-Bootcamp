# Day 22 — Quick Reference: Lists

## Creating lists
| Method | Example | Result |
|--------|---------|--------|
| Literal | `[1, 2, 3]` | `[1, 2, 3]` |
| From string | `list('abc')` | `['a', 'b', 'c']` |
| From range | `list(range(1, 6))` | `[1, 2, 3, 4, 5]` |
| Repetition | `[0] * 4` | `[0, 0, 0, 0]` |

## Indexing
| Pattern | Meaning |
|---------|---------|
| `a[0]` | First item |
| `a[-1]` | Last item |
| `a[-2]` | Second-to-last |
| `a[len(a)//2]` | Middle item |

## Slicing `a[start:stop:step]`
| Pattern | Meaning |
|---------|---------|
| `a[1:4]` | Items at index 1, 2, 3 |
| `a[:3]` | First 3 items |
| `a[-3:]` | Last 3 items |
| `a[::2]` | Every other item |
| `a[::-1]` | Reversed copy |
| `a[:]` | Full copy |

## Built-in functions
```python
len(a)   # number of items
min(a)   # smallest
max(a)   # largest
sum(a)   # total (numbers only)
```

## Membership
```python
'x' in a       # True if 'x' is in list
'x' not in a   # True if 'x' is NOT in list
```

## Copy vs alias
```python
b = a          # alias — same object, dangerous!
b = a.copy()   # independent copy
b = a[:]       # also an independent copy
```
