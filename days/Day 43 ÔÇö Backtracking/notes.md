# Day 43 — Backtracking

## Template
```python
def backtrack(path, choices):
    if done(path):
        result.append(path[:])  # copy!
        return
    for choice in choices:
        if valid(choice, path):
            path.append(choice)          # choose
            backtrack(path, new_choices) # explore
            path.pop()                   # un-choose
```

## Common problems
| Problem | Key idea |
|---------|---------|
| Permutations | Swap/pick from remaining |
| Combinations | Only move forward (avoid duplicates) |
| Subsets | Include or exclude each element |
| N-Queens | Track rows, cols, diagonals |
| Sudoku | Try 1-9 at each empty cell |

## Gotchas
- Always `.copy()` or `[:]` before appending to results
- Combinations: start from `start` index to avoid reordering
- Prune early: `if current_sum > target: return`

## Interview tips
- "Generate all..." → backtracking
- Prune aggressively to improve from exponential to manageable
- N-queens: use sets for O(1) conflict checking
