# Day 10 — Lists

## Key syntax
```python
lst = [1, 2, 3]

lst[0]      lst[-1]      lst[1:3]    lst[::-1]

lst.append(x)       lst.insert(i, x)
lst.remove(x)       lst.pop()       lst.pop(i)
lst.sort()          sorted(lst)
lst.reverse()       lst.copy()
len(lst)  sum(lst)  max(lst)  min(lst)
x in lst
```

## Gotchas
- `new = lst` → same object. Use `lst.copy()` or `lst[:]`
- `.sort()` returns `None`, `sorted()` returns a new list
- `in` is O(n) for lists — use a set for fast membership

## Interview tips
- "Remove duplicates preserving order" → seen set + loop
- Rotate: `lst[-n:] + lst[:-n]` — slicing solution
- Two Sum: store complements in a dict as you go — O(n)
