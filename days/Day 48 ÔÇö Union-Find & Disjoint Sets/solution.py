# Day 48 — Union-Find — SOLUTIONS
from collections import defaultdict

class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n)); self.rank=[0]*n; self._count=n
    def find(self,x):
        if self.parent[x]!=x: self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py: return False
        if self.rank[px]<self.rank[py]: px,py=py,px
        self.parent[py]=px
        if self.rank[px]==self.rank[py]: self.rank[px]+=1
        self._count-=1; return True
    def connected(self,x,y): return self.find(x)==self.find(y)
    @property
    def count(self): return self._count

def find_provinces(ic):
    n=len(ic); uf=UnionFind(n)
    for i in range(n):
        for j in range(i+1,n):
            if ic[i][j]: uf.union(i,j)
    return uf.count

def find_redundant(edges):
    n=len(edges); uf=UnionFind(n+1)
    for u,v in edges:
        if not uf.union(u,v): return [u,v]

def accounts_merge(accounts):
    email_to_id={}; uf=UnionFind(len(accounts)*10)
    for i,acc in enumerate(accounts):
        for email in acc[1:]:
            if email not in email_to_id: email_to_id[email]=i*10
            uf.union(i*10,email_to_id[email])
    groups=defaultdict(set)
    for email,eid in email_to_id.items():
        groups[uf.find(eid)].add(email)
    result=[]
    for gid,emails in groups.items():
        name=accounts[gid//10][0]
        result.append([name]+sorted(emails))
    return result

def equations_possible(equations):
    uf=UnionFind(26)
    for eq in equations:
        if eq[1]=='=': uf.union(ord(eq[0])-97,ord(eq[3])-97)
    for eq in equations:
        if eq[1]=='!' and uf.connected(ord(eq[0])-97,ord(eq[3])-97): return False
    return True

def min_spanning_tree(n,edges):
    edges.sort(key=lambda x:x[2]); uf=UnionFind(n); total=0
    for u,v,w in edges:
        if uf.union(u,v): total+=w
    return total
