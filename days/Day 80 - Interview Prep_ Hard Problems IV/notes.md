# Day 80 — Hard Problems IV — Review Day

## Complete algorithm cheat sheet

### Arrays & Strings
- Two sum → hash map O(n)
- Sliding window → variable or fixed size
- Longest substring → hash map + two pointers

### DP
- Fibonacci pattern: `dp[i] = dp[i-1] + dp[i-2]`
- Kadane's: `curr = max(x, curr+x)`
- LCS: `dp[i][j] = dp[i-1][j-1]+1 if match else max(dp[i-1][j], dp[i][j-1])`

### Graphs
- BFS for shortest path
- DFS for connected components, cycle detection
- Dijkstra for weighted shortest path
- Topo sort for ordering with dependencies

### Heap
- Kth largest → min-heap of size k
- Median → two heaps (max for lower, min for upper)
- Merge k sorted → heap with (val, list_idx)

### Binary search
- Classic: lo<=hi, check mid, move lo/hi
- Answer space: lo=min, hi=max, check feasibility

## Interview day tips
- Read the problem twice before coding
- Mention brute force, then optimise
- Always state time and space complexity
- Test with the examples + edge cases
- Don't panic — talk through your thinking
