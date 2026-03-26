# Day 44 — Greedy Algorithms

## When greedy works
- Coin change with standard denominations
- Activity selection / interval scheduling
- Huffman coding
- Jump game

## When greedy FAILS (use DP)
- Coin change with arbitrary denominations
- 0/1 Knapsack
- Longest increasing subsequence

## Common patterns
```python
# Activity selection (max non-overlapping)
activities.sort(key=lambda x: x[1])  # sort by END
for start, end in activities:
    if start >= last_end: count+=1; last_end=end

# Interval removal
intervals.sort(key=lambda x: x[1])
end=intervals[0][1]; removed=0
for s,e in intervals[1:]:
    if s<end: removed+=1
    else: end=e
```

## Gotchas
- Greedy needs proof — don't assume it works
- Sort direction matters: by start vs end vs other key
- Exchange argument: if swapping two adjacent elements can only improve, greedy is correct

## Interview tips
- "Minimum intervals to remove" → sort by end, keep as many non-overlapping as possible
- Jump Game → track max reachable index
- Queue reconstruction → sort tall people first, insert by k
