# 📋 Lists & Tuples

## Lists (mutable)
```python
lst = [1, 2, 3]
lst.append(4)           # add to end
lst.insert(1, 99)       # insert at index
lst.remove(99)          # remove first occurrence
lst.pop()               # removes & returns last
lst.pop(0)              # removes & returns index 0
lst.sort()              # in-place
sorted(lst)             # returns new sorted list
lst.index(2)            # index of value
lst.count(2)            # count occurrences
lst.extend([5, 6])      # append multiple
len(lst)                # length
```

## Slicing
```python
lst = [0, 1, 2, 3, 4]
lst[1:3]    # [1, 2]
lst[::2]    # [0, 2, 4] every 2nd
lst[::-1]   # reversed
```

## Tuples (immutable)
```python
t = (1, 2, 3)
a, b, c = t         # unpacking
first, *rest = t    # starred unpacking
```

## Gotchas
- Copy lists with lst.copy() not `new = lst`
- `in` is O(n) for lists, O(1) for sets
