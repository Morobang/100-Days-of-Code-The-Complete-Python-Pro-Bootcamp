# Day 37 — Heaps & Priority Queues

## Key syntax
```python
import heapq

heapq.heapify(lst)           # O(n) — in-place min-heap
heapq.heappush(heap, val)    # O(log n)
heapq.heappop(heap)          # O(log n) — min element
heapq.nsmallest(k, lst)      # k smallest O(n log k)
heapq.nlargest(k, lst)       # k largest

# Max-heap: negate values
heappush(heap, -val)
-heappop(heap)

# Priority queue with key
heappush(heap, (priority, item))
```

## Gotchas
- Python only has min-heap — negate for max-heap
- `heapify` modifies the list in-place
- Use `(priority, index, item)` if items aren't comparable

## Interview tips
- "Find kth largest" → min-heap of size k
- "Merge k sorted" → heap with (val, list_idx, item_idx)
- Median → two heaps: max-heap for lower half, min-heap for upper half
