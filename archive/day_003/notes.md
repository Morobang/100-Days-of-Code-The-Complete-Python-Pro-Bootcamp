# Day 003 — Lists

## Key syntax
```python
lst.append(x)       # add to end
lst.insert(i, x)    # insert at index i
lst.pop()           # remove & return last
lst.pop(0)          # remove & return first
lst.remove(x)       # remove first occurrence of x
lst.sort()          # sort in place
sorted(lst)         # return new sorted list
lst[::-1]           # reversed copy
lst[1:4]            # slice: indices 1,2,3
lst[::2]            # every 2nd element
len(lst)            # length
x in lst            # membership (O(n))
```

## Gotchas
- `new = lst` → same object, NOT a copy. Use `lst.copy()` or `lst[:]`
- `lst.sort()` modifies in place, returns `None`. `sorted(lst)` returns a new list
- `in` is O(n) for lists — if you need fast membership checks, use a set

## Interview tips
- Rotate: `lst[-n:] + lst[:-n]` — slicing solution is O(n), expected answer
- "Remove duplicates preserving order" → use a `seen` set + loop
- Know the difference between shallow copy (`lst.copy()`) and deep copy (`copy.deepcopy(lst)`)
