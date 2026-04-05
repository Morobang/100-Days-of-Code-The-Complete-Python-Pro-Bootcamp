# Day 71 — Divide and Conquer

## The pattern
```
D&C:
1. Divide:   split problem into smaller subproblems
2. Conquer:  solve each subproblem recursively
3. Combine:  merge solutions into final answer

Base case:   when subproblem is small enough to solve directly
```

## Key algorithms
```python
# Fast power — O(log n)
def fast_pow(b, e):
    if e == 0: return 1
    half = fast_pow(b, e // 2)
    return half * half if e % 2 == 0 else half * half * b

# Quickselect — O(n) average
def quickselect(lst, k):
    pivot = lst[len(lst)//2]
    lo = [x for x in lst if x < pivot]
    hi = [x for x in lst if x > pivot]
    mi = [x for x in lst if x == pivot]
    if k <= len(lo): return quickselect(lo, k)
    if k <= len(lo)+len(mi): return pivot
    return quickselect(hi, k-len(lo)-len(mi))
```

## Gotchas
- Always define the base case first — without it you'll recurse forever
- D&C overhead: splitting and merging costs extra time/space
- Quicksort worst case O(n²) — use random pivot or median-of-three

## Interview tips
- Fast power → O(log n) instead of O(n) looping
- Quickselect → kth largest/smallest in O(n) average
- Count inversions → merge sort variant (classic D&C trick)
