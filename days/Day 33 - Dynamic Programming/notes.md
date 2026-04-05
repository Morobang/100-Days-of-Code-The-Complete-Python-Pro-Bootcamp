# Day 33 — Dynamic Programming

## Key patterns
```python
# 1D DP
dp = [0] * (n+1)
dp[0] = base_case
for i in range(1, n+1):
    dp[i] = some_function(dp[i-1], dp[i-2], ...)

# 2D DP (LCS, knapsack)
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = ...

# Memoization shortcut
from functools import lru_cache
@lru_cache(maxsize=None)
def dp(i, j): ...
```

## Classic DP problems
| Problem | Recurrence |
|---------|-----------|
| Fibonacci | `dp[i] = dp[i-1] + dp[i-2]` |
| Stairs | `dp[i] = dp[i-1] + dp[i-2]` |
| House robber | `dp[i] = max(dp[i-1], dp[i-2]+h[i])` |
| Coin change | `dp[a] = min(dp[a], dp[a-c]+1)` |

## Interview tips
- If you see "how many ways" or "minimum cost" → think DP
- Start with recursion + memoization, then convert to tabulation
- Space optimisation: often only need last 1-2 rows
