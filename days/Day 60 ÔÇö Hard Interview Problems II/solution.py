# Day 60 — Hard Problems II — SOLUTIONS
from collections import defaultdict

def max_profit_k(k,prices):
    n=len(prices)
    if k>=n//2: return sum(max(0,prices[i+1]-prices[i]) for i in range(n-1))
    dp=[[0]*n for _ in range(k+1)]
    for t in range(1,k+1):
        max_so_far=-prices[0]
        for d in range(1,n):
            dp[t][d]=max(dp[t][d-1],prices[d]+max_so_far)
            max_so_far=max(max_so_far,dp[t-1][d]-prices[d])
    return dp[k][n-1]

def regex_match(s,p):
    m,n=len(s),len(p)
    dp=[[False]*(n+1) for _ in range(m+1)]; dp[0][0]=True
    for j in range(2,n+1):
        if p[j-1]=='*': dp[0][j]=dp[0][j-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[i][j]=dp[i][j-2] or (dp[i-1][j] and (p[j-2]=='.' or p[j-2]==s[i-1]))
            elif p[j-1]=='.' or p[j-1]==s[i-1]: dp[i][j]=dp[i-1][j-1]
    return dp[m][n]

def max_sum_rectangle(matrix):
    rows,cols=len(matrix),len(matrix[0]); best=float('-inf')
    for l in range(cols):
        sums=[0]*rows
        for r in range(l,cols):
            for i in range(rows): sums[i]+=matrix[i][r]
            curr=best_so_far=sums[0]
            for x in sums[1:]: curr=max(x,curr+x); best_so_far=max(best_so_far,curr)
            best=max(best,best_so_far)
    return best

def num_decodings(s):
    if not s or s[0]=='0': return 0
    dp=[0]*(len(s)+1); dp[0]=dp[1]=1
    for i in range(2,len(s)+1):
        if s[i-1]!='0': dp[i]+=dp[i-1]
        two=int(s[i-2:i])
        if 10<=two<=26: dp[i]+=dp[i-2]
    return dp[len(s)]

def critical_connections(n,connections):
    graph=defaultdict(list)
    for u,v in connections: graph[u].append(v); graph[v].append(u)
    disc=[-1]*n; low=[0]*n; bridges=[]; timer=[0]
    def dfs(u,parent):
        disc[u]=low[u]=timer[0]; timer[0]+=1
        for v in graph[u]:
            if disc[v]==-1:
                dfs(v,u); low[u]=min(low[u],low[v])
                if low[v]>disc[u]: bridges.append([u,v])
            elif v!=parent: low[u]=min(low[u],disc[v])
    for i in range(n):
        if disc[i]==-1: dfs(i,-1)
    return bridges

def longest_increasing_path(matrix):
    if not matrix: return 0
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

def count_range_sum(nums,lower,upper):
    from sortedcontainers import SortedList
    sl=SortedList([0]); prefix=count=0
    for n in nums:
        prefix+=n
        count+=sl.bisect_right(prefix-lower)-sl.bisect_left(prefix-upper)
        sl.add(prefix)
    return count

def max_coins(nums):
    nums=[1]+nums+[1]; n=len(nums)
    dp=[[0]*n for _ in range(n)]
    for l in range(2,n):
        for left in range(n-l):
            right=left+l
            for k in range(left+1,right):
                dp[left][right]=max(dp[left][right],dp[left][k]+dp[k][right]+nums[left]*nums[k]*nums[right])
    return dp[0][n-1]
