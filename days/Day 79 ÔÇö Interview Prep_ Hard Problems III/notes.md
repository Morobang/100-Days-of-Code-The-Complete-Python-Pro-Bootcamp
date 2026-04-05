# Day 79 — Hard Problems III

## Advanced techniques at a glance
```python
# Longest path in DAG (memo DFS)
def dfs(r, c):
    if (r, c) in memo: return memo[(r, c)]
    best = 1
    for each valid neighbour (nr, nc):
        best = max(best, 1 + dfs(nr, nc))
    memo[(r, c)] = best; return best

# Job scheduling (DP + binary search)
jobs = sorted(zip(end, start, profit))
dp = [(0, 0)]   # (end_time, max_profit)
for e, s, p in jobs:
    prev = bisect_right(dp, (s, float('inf'))) - 1
    if dp[prev][1] + p > dp[-1][1]:
        dp.append((e, dp[prev][1] + p))

# Expression operators (backtracking)
def bt(idx, curr_val, last, path):
    if idx == len(num):
        if curr_val == target: results.append(path)
        return
    for i in range(idx+1, len(num)+1):
        segment = num[idx:i]
        if len(segment) > 1 and segment[0] == '0': break
        n = int(segment)
        if idx == 0: bt(i, n, n, segment)
        else:
            bt(i, curr_val+n, n, path+'+'+segment)
            bt(i, curr_val-n, -n, path+'-'+segment)
            bt(i, curr_val-last+last*n, last*n, path+'*'+segment)
```
