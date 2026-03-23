# Day 08 — Loops: for & range

## Key syntax
```python
for item in iterable: ...

range(n)              # 0 to n-1
range(start, stop)
range(start, stop, step)

enumerate(lst)         # (index, value)
enumerate(lst, start=1) # start index at 1
zip(a, b)              # pairs
reversed(lst)
sorted(lst)

break     # exit loop
continue  # skip to next
```

## Gotchas
- `range(5)` = 0,1,2,3,4 — does NOT include 5
- `for i in range(len(lst))` is often worse than `for item in lst`
- Modifying a list while iterating it → bugs

## Interview tips
- FizzBuzz: `%15` before `%3` and `%5`
- `enumerate()` shows Python fluency — use it over manual index
- `zip()` for processing two related lists together
