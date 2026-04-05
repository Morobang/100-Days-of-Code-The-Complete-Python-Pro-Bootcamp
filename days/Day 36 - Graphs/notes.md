# Day 36 — Graphs

## Representations
```python
# Adjacency list (most common)
graph = {node: [neighbours]}

# Build from edge list
from collections import defaultdict
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected
```

## DFS vs BFS
| | DFS | BFS |
|---|---|---|
| Data structure | Stack (or recursion) | Queue |
| Use for | Paths, cycles, components | Shortest path (unweighted) |
| Memory | O(depth) | O(width) |

## Key templates
```python
# DFS iterative
stack = [start]; visited = {start}
while stack:
    node = stack.pop()
    for n in graph[node]:
        if n not in visited: visited.add(n); stack.append(n)

# BFS
q = deque([start]); visited = {start}
while q:
    node = q.popleft()
    for n in graph[node]:
        if n not in visited: visited.add(n); q.append(n)
```

## Interview tips
- Always track `visited` to avoid infinite loops
- Islands → DFS/BFS from each unvisited land cell
- Cycle detection → track parent in DFS
- Topological sort → Kahn's algorithm (BFS + in-degree)
