# Day 45 — Interval Problems

## Key patterns
```python
# Merge: sort by start, track last end
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for s, e in intervals[1:]:
    if s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])

# Meeting rooms II: sweep line
import heapq
intervals.sort(key=lambda x: x[0])
heap = []  # end times
for s, e in intervals:
    if heap and heap[0] <= s: heapq.heapreplace(heap, e)
    else: heapq.heappush(heap, e)
return len(heap)

# Two-pointer for overlaps
intervals.sort()
i, j = 0, 1
while j < len(intervals): ...
```

## Gotchas
- Always sort before processing
- Merge: `merged[-1][1] = max(...)` not just `= e`
- Meeting rooms: use a min-heap of end times

## Interview tips
- "How many rooms needed" → heap of end times (classic)
- Insert interval: three phases — before, overlap, after
- Employee free time: merge all, find gaps
