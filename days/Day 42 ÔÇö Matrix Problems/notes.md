# Day 42 — Matrix Problems

## Key patterns
```python
rows, cols = len(m), len(m[0])

# 4-directional moves
for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r+dr, c+dc
    if 0<=nr<rows and 0<=nc<cols: ...

# Transpose
[[m[r][c] for r in range(rows)] for c in range(cols)]

# Rotate 90° clockwise
# Step 1: transpose
# Step 2: reverse each row

# Spiral: peel off top row, rotate remaining
while matrix:
    result += matrix.pop(0)
    matrix = list(zip(*matrix))[::-1]
```

## Gotchas
- Always bounds-check: `0<=r<rows and 0<=c<cols`
- Rotating in-place: transpose then reverse rows
- DFS on grid: mark visited by modifying cell (restore after if needed)

## Interview tips
- Search in sorted matrix: start top-right, go left/down
- Word search: DFS with backtracking (restore cell after visit)
- Maximal square: DP — `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`
