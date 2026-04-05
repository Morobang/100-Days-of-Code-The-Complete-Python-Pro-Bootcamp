# Day 36 — Graphs — SOLUTIONS
from collections import deque, defaultdict

def dfs_order(graph,start):
    visited=[]; seen=set()
    def dfs(node):
        seen.add(node); visited.append(node)
        for n in graph.get(node,[]):
            if n not in seen: dfs(n)
    dfs(start); return visited

def bfs_order(graph,start):
    visited=[start]; seen={start}; q=deque([start])
    while q:
        node=q.popleft()
        for n in graph.get(node,[]):
            if n not in seen: seen.add(n); visited.append(n); q.append(n)
    return visited

def has_path(graph,src,dst):
    if src==dst: return True
    seen={src}; stack=[src]
    while stack:
        node=stack.pop()
        for n in graph.get(node,[]):
            if n==dst: return True
            if n not in seen: seen.add(n); stack.append(n)
    return False

def shortest_path(graph,src,dst):
    q=deque([(src,0)]); seen={src}
    while q:
        node,dist=q.popleft()
        if node==dst: return dist
        for n in graph.get(node,[]):
            if n not in seen: seen.add(n); q.append((n,dist+1))
    return -1

def count_components(n,edges):
    parent=list(range(n))
    def find(x): return x if parent[x]==x else find(parent[x])
    def union(a,b): parent[find(a)]=find(b)
    for a,b in edges: union(a,b)
    return len({find(i) for i in range(n)})

def has_cycle(graph):
    visited=set()
    def dfs(node,parent):
        visited.add(node)
        for n in graph.get(node,[]):
            if n not in visited:
                if dfs(n,node): return True
            elif n!=parent: return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node,None): return True
    return False

def num_islands(grid):
    if not grid: return 0
    rows,cols=len(grid),len(grid[0]); count=0
    def dfs(r,c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1': return
        grid[r][c]='0'
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]: dfs(r+dr,c+dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1': dfs(r,c); count+=1
    return count

def topo_sort(n,prerequisites):
    graph=defaultdict(list); indegree=[0]*n
    for a,b in prerequisites: graph[b].append(a); indegree[a]+=1
    q=deque([i for i in range(n) if indegree[i]==0]); order=[]
    while q:
        node=q.popleft(); order.append(node)
        for n2 in graph[node]:
            indegree[n2]-=1
            if indegree[n2]==0: q.append(n2)
    return order if len(order)==n else []
