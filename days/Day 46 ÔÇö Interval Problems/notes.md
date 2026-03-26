# Day 46 — Interval Problems

## Key patterns
```python
# Merge intervals
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for s, e in intervals[1:]:
    if s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])

# Insert interval
result = []
i = 0
# Add all before new
while i < len(intervals) and intervals[i][1] < new[0]:
    result.append(intervals[i]); i += 1
# Merge overlapping
while i < len(intervals) and intervals[i][0] <= new[1]:
    new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]; i += 1
result.append(new)
# Add remaining
result += intervals[i:]
```

## Gotchas
- Sort by start time before merging
- Overlap condition: `start_b <= end_a` (not strict `<`)
- For min rooms/resources: use event sweep (sort starts+ends separately)

## Interview tips
- Calendar/scheduling → interval merge
- "How many rooms needed?" → sweep events, track active count
- Two-pointer for interval intersection of two sorted lists
