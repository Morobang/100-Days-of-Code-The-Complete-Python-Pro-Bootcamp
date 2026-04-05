# Day 10 — Lists

## Key syntax
```python
lst = [1, 2, 3]

# Access
lst[0]         # first
lst[-1]        # last
lst[1:3]       # slice
lst[::-1]      # reversed copy

# Modify
lst.append(x)
lst.insert(i, x)
lst.remove(x)    # removes first occurrence
lst.pop()        # removes & returns last
lst.pop(i)       # removes & returns index i
lst.sort()       # in place
sorted(lst)      # new sorted list
lst.reverse()    # in place

# Info
len(lst)
sum(lst)
max(lst)
min(lst)
x in lst

# Copy (important!)
copy = lst.copy()   # NOT: copy = lst
```

## Gotchas
- `new = lst` does NOT copy — both variables point to the same list
- `.sort()` returns `None`, `sorted()` returns a new list
- Removing from a list while looping it → bugs. Loop a copy: `for x in lst[:]:`

## Interview tips
- "Remove duplicates preserving order" → `seen` set + loop (not just `list(set(...))`)
- Lists are O(n) for `in` checks — use a set for fast membership testing
- Know slicing cold — it comes up in almost every Python interview
