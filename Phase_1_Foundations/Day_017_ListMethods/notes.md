# Day 17 — Quick Reference

## Sorting

```python
nums = [3, 1, 4, 1, 5, 9]
nums.sort()              # modifies nums in-place → [1, 1, 3, 4, 5, 9]
nums.sort(reverse=True)  # descending → [9, 5, 4, 3, 1, 1]

# sorted() returns a NEW list — original unchanged
original = [3, 1, 2]
new = sorted(original)   # [1, 2, 3]
print(original)          # [3, 1, 2]  — unchanged
```

## Reversing

```python
nums = [1, 2, 3]
nums.reverse()    # [3, 2, 1]  — in-place
```

## count() and index()

```python
items = ['a', 'b', 'a', 'c', 'a']
items.count('a')    # 3  — how many times 'a' appears
items.index('b')    # 1  — index of first 'b'
items.index('z')    # ValueError if not found
```

## pop() and insert()

```python
nums = [1, 2, 3, 4]
nums.pop()       # removes and returns last item → 4, list is now [1, 2, 3]
nums.pop(0)      # removes and returns item at index 0 → 1, list is now [2, 3]

nums = [1, 3, 4]
nums.insert(1, 99)    # insert 99 at index 1 → [1, 99, 3, 4]
```

## remove()

```python
nums = [1, 2, 3, 2]
nums.remove(2)    # removes FIRST occurrence of 2 → [1, 3, 2]
```

## min(), max(), sum()

```python
nums = [3, 1, 4, 1, 5]
min(nums)    # 1
max(nums)    # 5
sum(nums)    # 14
```

## copy()

```python
a = [1, 2, 3]
b = a          # b points to the SAME list — changes to b affect a
b = a.copy()   # b is an independent copy — safe to modify
```

## Gotchas

- `.sort()` modifies the list in-place and returns `None`. Do NOT do `x = x.sort()` — you will lose the list.
- Use `sorted(x)` when you want a new sorted copy and need to keep the original.
- `.index()` raises `ValueError` if the item is not found — check with `in` first if unsure.
- `.pop()` with no argument removes the **last** item (very common pattern).
