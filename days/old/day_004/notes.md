# Day 004 — List Methods & Slicing

## Key syntax
```python
lst[start:stop:step]  # full slice syntax
lst[::-1]             # reverse
lst[::2]              # every 2nd
lst[-3:]              # last 3

# Copying
lst.copy()            # shallow copy
lst[:]                # also shallow copy
import copy
copy.deepcopy(lst)    # deep copy (nested structures)

# Sorting with key
lst.sort(key=lambda x: x[1])      # sort by second element
sorted(lst, key=len, reverse=True) # sort strings by length, desc
```

## Gotchas
- Slicing never raises `IndexError` — `lst[100:]` returns `[]`
- `sorted()` works on any iterable; `.sort()` only on lists
- Step can be negative: `lst[8:2:-1]` walks backwards from 8 to 3

## Interview tips
- "Rotate array in place" — classic follow-up: can you do it O(1) space? (reverse sub-arrays trick)
- Transpose is foundational for any 2D grid / matrix problem
- "Two sum" problem uses a seen-set pattern — same idea as deduplicate
