# Day 22 — Sorting Algorithms

## Big O comparison
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) |
| Selection | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion | O(n) | O(n²) | O(n²) | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) |

## Python's sort
```python
lst.sort()                        # in-place, stable
sorted(lst)                       # new list
sorted(lst, reverse=True)
sorted(lst, key=lambda x: x[1])  # sort by second element
sorted(lst, key=lambda x: (-x[1], x[0]))  # multi-key
```

## Gotchas
- Bubble/Selection/Insertion are O(n²) — never use on large data
- Merge sort is stable — equal elements keep their relative order
- Python's built-in sort uses Timsort — O(n log n) always

## Interview tips
- Know the Big O of each by heart
- "What's the most efficient sort?" → Timsort/Merge for general use
- Insertion sort wins on small or nearly-sorted arrays
