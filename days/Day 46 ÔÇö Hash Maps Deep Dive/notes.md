# Day 46 — Hash Maps Deep Dive

## How a hash map works
1. Hash the key → bucket index
2. Handle collisions (chaining: list per bucket; open addressing: probe)
3. Resize when load factor too high

## Key patterns
```python
from collections import defaultdict, Counter, OrderedDict

# Frequency
Counter(lst)
Counter.most_common(k)

# Group by
groups = defaultdict(list)
groups[key].append(item)

# LRU Cache (O(1) get/put)
# → doubly linked list + hash map
# OR → OrderedDict
from collections import OrderedDict
cache = OrderedDict()
cache.move_to_end(key)
cache.popitem(last=False)  # remove oldest
```

## Gotchas
- Python dict is O(1) amortised — hash collisions rare with good hash
- `defaultdict` vs `setdefault` — same idea, defaultdict cleaner
- LRU Cache: dict for O(1) lookup + linked list for O(1) reorder

## Interview tips
- "O(1) insert/lookup/delete" → hash map
- "Count frequency" → Counter
- "Group items" → defaultdict(list)
