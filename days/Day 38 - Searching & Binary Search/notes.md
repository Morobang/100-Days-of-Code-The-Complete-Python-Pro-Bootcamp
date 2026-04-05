# Day 38 — Binary Search

## Template
```python
def binary_search(lst, target):
    lo, hi = 0, len(lst)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if lst[mid] == target: return mid
        elif lst[mid] < target: lo = mid+1
        else: hi = mid-1
    return -1
```

## Variants
```python
# Find first occurrence
while lo <= hi:
    mid = (lo+hi)//2
    if lst[mid] == target: result=mid; hi=mid-1  # go left
    ...

# Find last occurrence
    if lst[mid] == target: result=mid; lo=mid+1  # go right

# Answer-space binary search
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo+hi)//2
    if feasible(mid): hi = mid
    else: lo = mid+1
```

## Gotchas
- `lo <= hi` for exact search, `lo < hi` for boundary problems
- `mid = lo + (hi-lo)//2` avoids overflow (Python doesn't overflow but good habit)
- Rotated array: always one half is sorted — find which one

## Interview tips
- "O(log n) search" → binary search
- "Find minimum satisfying some condition" → binary search on answer
- Koko eating bananas, ship packages — same binary search on answer pattern
