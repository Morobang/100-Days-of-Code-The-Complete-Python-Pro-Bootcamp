# Day 23 — Quick Reference: List Methods

## Adding items
```python
a.append(x)      # adds x as one item at the end
a.extend(iter)   # adds each item from iter individually
a.insert(i, x)   # inserts x at index i
```

## Removing items
| Method | By | Returns |
|--------|----|---------|
| `a.remove(x)` | Value (first match) | `None` |
| `a.pop()` | Last index | Removed item |
| `a.pop(i)` | Index i | Removed item |
| `del a[i]` | Index i | Nothing |
| `del a[i:j]` | Slice | Nothing |

## Sorting
```python
a.sort()                    # sort in place, A-Z
a.sort(reverse=True)        # sort in place, Z-A
a.sort(key=len)             # sort in place, by length
a.sort(key=str.lower)       # case-insensitive sort

sorted(a)                   # returns new sorted list (a unchanged)
sorted(a, reverse=True)     # new list, reversed
sorted(a, key=len)          # new list, by key
```

## Stack (LIFO)
```python
stack = []
stack.append(x)   # push
stack.pop()       # pop (last item)
```

## Queue (FIFO)
```python
queue = []
queue.append(x)   # enqueue
queue.pop(0)      # dequeue (first item)
```

## Other
```python
a.clear()         # empty the list, a becomes []
```
