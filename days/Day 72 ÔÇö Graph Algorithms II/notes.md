# Day 72 — Graph Algorithms II

## Dijkstra — O((V+E) log V)
```python
import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float('inf')): continue
        for nbr, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nbr, float('inf')):
                dist[nbr] = nd
                heapq.heappush(heap, (nd, nbr))
    return dist
```

## Union-Find — O(α(n)) ≈ O(1) per operation
```python
def find(x):   # path compression
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):   # union by rank
    px, py = find(x), find(y)
    if rank[px] < rank[py]: px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]: rank[px] += 1
```

## Kruskal's MST — O(E log E)
1. Sort edges by weight
2. For each edge: add if it doesn't create a cycle (Union-Find)
3. Stop when n-1 edges added

## Interview tips
- Dijkstra: can't handle negative weights → use Bellman-Ford
- Union-Find: connectivity, cycle detection, Kruskal's MST
- Course schedule = topological sort = detect cycle in directed graph
