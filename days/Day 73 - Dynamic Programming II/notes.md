# Day 73 — Dynamic Programming II

## DP patterns summary
| Pattern | When to use | Example |
|---------|-------------|---------|
| 1D DP | Linear state | Fibonacci, stairs |
| 2D DP | Two dimensions | LCS, edit distance |
| Interval DP | Optimal split | Matrix chain, burst balloons |
| State machine | Finite states | Stock trading variants |
| Digit DP | Count integers | Numbers with digit constraint |
| Bitmask DP | Subset state | TSP, assignment |

## State machine template
```python
# General: define states, write transitions
state_a, state_b, state_c = init
for x in data:
    state_a, state_b, state_c = (
        transition_to_a(state_a, state_b, state_c, x),
        transition_to_b(state_a, state_b, state_c, x),
        transition_to_c(state_a, state_b, state_c, x),
    )
```

## Interval DP template
```python
dp = [[0]*n for _ in range(n)]
for length in range(2, n+1):          # all lengths
    for i in range(n-length+1):       # all start positions
        j = i + length - 1            # end position
        for k in range(i, j):         # all split points
            dp[i][j] = max/min(dp[i][j], dp[i][k]+dp[k+1][j]+cost)
```

## Interview tips
- When you see "optimal way to split/merge intervals" → interval DP
- State machine DP: draw the states and transitions first
- Space optimisation: if dp[i] only depends on dp[i-1], use two variables
