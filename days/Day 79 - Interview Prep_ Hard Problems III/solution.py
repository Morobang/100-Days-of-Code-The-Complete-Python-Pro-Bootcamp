# Day 79 — Hard Problems III — SOLUTIONS
import heapq, bisect
from math import comb

def lip(matrix):
    rows,cols=len(matrix),len(matrix[0]); memo={}
    def dfs(r,c):
        if (r,c) in memo: return memo[(r,c)]
        best=1
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]>matrix[r][c]:
                best=max(best,1+dfs(nr,nc))
        memo[(r,c)]=best; return best
    return max(dfs(r,c) for r in range(rows) for c in range(cols))

def job_scheduling(startTime,endTime,profit):
    jobs=sorted(zip(endTime,startTime,profit))
    dp=[(0,0)]
    for e,s,p in jobs:
        i=bisect.bisect_right(dp,(s,float('inf')))-1
        if dp[i][1]+p>dp[-1][1]: dp.append((e,dp[i][1]+p))
    return dp[-1][1]

def count_reorders(nums):
    MOD=10**9+7
    def count(arr):
        if len(arr)<=2: return 1
        root=arr[0]
        left=[x for x in arr[1:] if x<root]
        right=[x for x in arr[1:] if x>root]
        return comb(len(left)+len(right),len(left))*count(left)*count(right)%MOD
    return (count(nums)-1)%MOD

def min_cost_connect(points):
    n=len(points); visited=[False]*n; dist=[float('inf')]*n; dist[0]=0; cost=0
    for _ in range(n):
        u=min((i for i in range(n) if not visited[i]),key=lambda i:dist[i])
        visited[u]=True; cost+=dist[u]
        for v in range(n):
            if not visited[v]:
                d=abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])
                dist[v]=min(dist[v],d)
    return cost

def find_anagrams(s,p):
    pc=__import__('collections').Counter(p); wc=__import__('collections').Counter(s[:len(p)])
    result=[0] if wc==pc else []
    for i in range(len(p),len(s)):
        wc[s[i]]+=1; wc[s[i-len(p)]]-=1
        if wc[s[i-len(p)]]==0: del wc[s[i-len(p)]]
        if wc==pc: result.append(i-len(p)+1)
    return result

def min_path_triangle(t):
    dp=t[-1][:]
    for row in reversed(t[:-1]):
        dp=[row[i]+min(dp[i],dp[i+1]) for i in range(len(row))]
    return dp[0]

def stone_game(piles): return True  # Alice always wins with optimal play (provable by DP)

def add_operators(num,target):
    results=[]
    def bt(idx,curr,last,path):
        if idx==len(num):
            if curr==target: results.append(path); return
        for i in range(idx+1,len(num)+1):
            seg=num[idx:i]
            if len(seg)>1 and seg[0]=='0': break
            n=int(seg)
            if idx==0: bt(i,n,n,seg)
            else:
                bt(i,curr+n,n,path+'+'+seg)
                bt(i,curr-n,-n,path+'-'+seg)
                bt(i,curr-last+last*n,last*n,path+'*'+seg)
    bt(0,0,0,''); return results
