# Day 08 — Loops: for & range

## Key syntax
```python
for item in iterable:
    ...

range(n)           # 0 to n-1
range(start, stop) # start to stop-1
range(start, stop, step)

# Useful built-ins with for
enumerate(lst)           # (index, value) pairs
zip(lst1, lst2)          # pairs from two lists
reversed(lst)            # iterate backwards
sorted(lst)              # iterate in sorted order

# Loop control
break       # exit loop
continue    # skip to next iteration
```

## Gotchas
- `range(5)` → 0,1,2,3,4 — does NOT include 5
- `for i in range(len(lst))` is often worse than `for item in lst` or `enumerate(lst)`
- Modifying a list while iterating it → unexpected behaviour — iterate a copy instead

## Interview tips
- FizzBuzz: check `% 15` first, then `% 3`, then `% 5` — order matters
- `enumerate()` shows Python fluency — use it instead of manual index tracking
- Know the difference: `for` = known iterations, `while` = condition-based
