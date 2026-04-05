# Day 34 — Two Pointers & Sliding Window

## Two pointers patterns
```python
# Opposite ends (sorted array)
l, r = 0, len(lst)-1
while l < r:
    if condition: return (l, r)
    elif too_small: l += 1
    else: r -= 1

# Same direction (fast/slow)
slow = 0
for fast in range(len(lst)):
    if keep(lst[fast]):
        lst[slow] = lst[fast]; slow += 1
return slow  # new length
```

## Sliding window patterns
```python
# Fixed size k
window = sum(lst[:k])
for i in range(k, len(lst)):
    window += lst[i] - lst[i-k]

# Variable size (shrink when condition met)
l = total = 0
for r in range(len(lst)):
    total += lst[r]
    while total >= target:
        result = min(result, r-l+1)
        total -= lst[l]; l += 1
```

## Interview tips
- Two pointers on sorted array → usually O(n) vs O(n²) brute force
- Sliding window: "longest/shortest subarray with property X"
- Three sum: fix one element, two-pointer the rest
