# Day 48 — Union-Find

## Implementation
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):         # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):     # union by rank
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px,py = py,px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px]+=1
        return True
```

## Complexity
- With path compression + union by rank: nearly O(1) per operation — O(α(n))
- Building: O(n)
- m operations: O(m · α(n)) ≈ O(m)

## Gotchas
- Always `find()` before comparing parents
- `union()` returns False if already connected (useful for cycle detection)
- For non-integer keys: map to integers first

## Interview tips
- Cycle detection in undirected graph: if `union()` returns False → cycle
- Connected components: count roots (nodes where `parent[x] == x`)
- Kruskal's MST: sort edges by weight, union greedily
