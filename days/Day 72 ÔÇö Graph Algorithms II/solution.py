# Day 72 — Graph Algorithms II — SOLUTIONS
import heapq
from collections import defaultdict, deque

def dijkstra(graph,start):
    dist={start:0}; heap=[(0,start)]
    while heap:
        d,node=heapq.heappop(heap)
        if d>dist.get(node,float('inf')): continue
        for nbr,w in graph.get(node,[]):
            nd=d+w
            if nd<dist.get(nbr,float('inf')): dist[nbr]=nd; heapq.heappush(heap,(nd,nbr))
    return dist

def shortest_path(graph,start,end):
    dist={start:0}; prev={start:None}; heap=[(0,start)]
    while heap:
        d,node=heapq.heappop(heap)
        if node==end:
            path=[]; cur=end
            while cur: path.append(cur); cur=prev[cur]
            return d,path[::-1]
        if d>dist.get(node,float('inf')): continue
        for nbr,w in graph.get(node,[]):
            nd=d+w
            if nd<dist.get(nbr,float('inf')): dist[nbr]=nd; prev[nbr]=node; heapq.heappush(heap,(nd,nbr))
    return float('inf'),[]

class UnionFind:
    def __init__(self,n): self.parent=list(range(n)); self.rank=[0]*n
    def find(self,x):
        if self.parent[x]!=x: self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py: return False
        if self.rank[px]<self.rank[py]: px,py=py,px
        self.parent[py]=px
        if self.rank[px]==self.rank[py]: self.rank[px]+=1
        return True

def kruskal(n,edges):
    uf=UnionFind(n); mst=[]; edges=sorted(edges)
    for w,u,v in edges:
        if uf.union(u,v): mst.append((w,u,v))
        if len(mst)==n-1: break
    return mst

def network_delay(times,n,k):
    graph=defaultdict(list)
    for u,v,w in times: graph[u].append((v,w))
    dist=dijkstra(graph,k)
    if len(dist)<n: return -1
    return max(dist.values())

def cheapest_flights(n,flights,src,dst,k):
    prices=[float('inf')]*n; prices[src]=0
    for _ in range(k+1):
        tmp=prices[:]
        for u,v,w in flights:
            if prices[u]!=float('inf') and prices[u]+w<tmp[v]: tmp[v]=prices[u]+w
        prices=tmp
    return prices[dst] if prices[dst]!=float('inf') else -1

def can_finish(n_courses,prerequisites):
    graph=defaultdict(list); indegree=[0]*n_courses
    for a,b in prerequisites: graph[b].append(a); indegree[a]+=1
    q=deque([i for i in range(n_courses) if indegree[i]==0]); count=0
    while q:
        node=q.popleft(); count+=1
        for n in graph[node]: indegree[n]-=1; (q.append(n) if indegree[n]==0 else None)
    return count==n_courses

def find_itinerary(tickets):
    graph=defaultdict(list)
    for src,dst in sorted(tickets,reverse=True): graph[src].append(dst)
    result=[]
    def dfs(airport):
        while graph[airport]: dfs(graph[airport].pop())
        result.append(airport)
    dfs('JFK'); return result[::-1]
