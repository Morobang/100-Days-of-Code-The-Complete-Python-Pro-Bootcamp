# Day 24 — Array & List Problems

## Key patterns
```python
# Two pointers (sorted array)
left, right = 0, len(lst)-1
while left < right: ...

# Sliding window (fixed size k)
window = sum(lst[:k])
for i in range(k, len(lst)):
    window += lst[i] - lst[i-k]

# Hash map for O(n) lookups
seen = {}
for i, x in enumerate(lst):
    complement = target - x
    if complement in seen: return (seen[complement], i)
    seen[x] = i

# Kadane's algorithm (max subarray)
curr = best = lst[0]
for x in lst[1:]:
    curr = max(x, curr+x)
    best = max(best, curr)
```

## Gotchas
- "Rotate right by k" → `lst[-k:] + lst[:-k]`
- Handle `k = 0` and `k >= len(lst)` for rotation
- Merge intervals: sort by start first

## Interview tips
- Two Sum → hash map O(n) not nested loop O(n²)
- Max subarray → Kadane's algorithm — know it by heart
- Product except self → prefix and suffix products trick
