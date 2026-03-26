# Day 25 — Dictionary & Hashing Problems

## Key tools
```python
from collections import Counter, defaultdict

Counter(lst)              # frequency map
Counter.most_common(n)    # top n elements
defaultdict(list)         # dict with default value
defaultdict(int)          # dict with 0 as default

# Prefix sum + hash map (subarray sum = k)
prefix=0; seen={0:1}
for x in lst:
    prefix+=x
    count+=seen.get(prefix-k,0)
    seen[prefix]=seen.get(prefix,0)+1
```

## Gotchas
- `defaultdict(list)` vs `{}.setdefault(k,[])`  — same idea
- Prefix sum trick converts O(n²) subarray problems to O(n)
- Set operations (`&`, `|`, `-`) are often cleaner than dict for membership

## Interview tips
- "Two Sum" → hash map, O(n) — must know by heart
- Frequency map → Counter → most_common()
- Sliding window + hash map → substring problems
