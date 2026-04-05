# Day 60 — Hard Interview Problems II

## Problem index
| Problem | Pattern |
|---------|---------|
| Stock k transactions | DP — states for buy/sell |
| Regex matching | 2D DP |
| Max sum rectangle | Kadane's on columns |
| Critical connections | Tarjan's bridge algorithm |
| Longest increasing path | DFS + memoization |
| Burst balloons | Interval DP |

## Key DP patterns at a glance
```python
# Interval DP (burst balloons)
for length in range(2, n+1):
    for left in range(n-length+1):
        right = left + length - 1
        for k in range(left+1, right):
            dp[left][right] = max(dp[left][right],
                                  dp[left][k] + dp[k][right] + ...)

# State machine DP (stock problems)
hold = max(hold, rest-price)
sold = hold + price
rest = max(rest, sold)
```

## Interview tips
- Burst balloons → "last balloon to burst" framing (classic trick)
- Regex matching → `*` means zero or more of PREVIOUS, not current
- Bridges → Tarjan's: back edge detection with discovery and low time
