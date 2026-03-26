# Day 47 — Advanced Hashing

## Key tools
```python
from collections import Counter, defaultdict, OrderedDict
from math import gcd

Counter('hello')            # {'l':2,'h':1,'e':1,'o':1}
Counter.most_common(k)      # top k
c1 + c2                     # merge counters
c1 - c2                     # subtract (negatives removed)
c1 & c2                     # min of each count
c1 | c2                     # max of each count

defaultdict(list)           # dd[key].append() without KeyError
defaultdict(lambda: defaultdict(int))  # nested

# Prefix sum with hash map
prefix=0; seen={0:1}
for x in lst:
    prefix+=x
    count+=seen.get(prefix-k,0)
    seen[prefix]=seen.get(prefix,0)+1
```

## Gotchas
- `Counter` subtraction ignores negatives/zeros
- `defaultdict` is faster than `dict.setdefault`
- For slope in max_points: normalise with GCD, handle vertical lines

## Interview tips
- Anagram → sort chars as key: `tuple(sorted(word))`
- Contiguous array → treat 0 as -1, find longest subarray with sum 0
- Two-map isomorphism → map both directions to catch `ab → aa` false positives
