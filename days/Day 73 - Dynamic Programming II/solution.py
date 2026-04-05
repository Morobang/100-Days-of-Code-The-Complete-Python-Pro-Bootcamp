# Day 73 — DP II — SOLUTIONS

def min_cut(s):
    n=len(s)
    is_pal=[[False]*n for _ in range(n)]
    for i in range(n): is_pal[i][i]=True
    for i in range(n-1):
        if s[i]==s[i+1]: is_pal[i][i+1]=True
    for l in range(3,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if s[i]==s[j]: is_pal[i][j]=is_pal[i+1][j-1]
    dp=[0]*n
    for i in range(n):
        if is_pal[0][i]: dp[i]=0; continue
        dp[i]=i
        for j in range(1,i+1):
            if is_pal[j][i]: dp[i]=min(dp[i],dp[j-1]+1)
    return dp[n-1]

def egg_drop(eggs,floors):
    dp=[[0]*(floors+1) for _ in range(eggs+1)]
    for f in range(1,floors+1): dp[1][f]=f
    for e in range(2,eggs+1):
        for f in range(1,floors+1):
            dp[e][f]=float('inf')
            for x in range(1,f+1):
                worst=1+max(dp[e-1][x-1],dp[e][f-x])
                dp[e][f]=min(dp[e][f],worst)
    return dp[eggs][floors]

def min_health(dungeon):
    rows,cols=len(dungeon),len(dungeon[0])
    dp=[[0]*cols for _ in range(rows)]
    for i in range(rows-1,-1,-1):
        for j in range(cols-1,-1,-1):
            if i==rows-1 and j==cols-1: dp[i][j]=max(1,1-dungeon[i][j])
            elif i==rows-1: dp[i][j]=max(1,dp[i][j+1]-dungeon[i][j])
            elif j==cols-1: dp[i][j]=max(1,dp[i+1][j]-dungeon[i][j])
            else: dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])
    return dp[0][0]

def paint_fence(n,k):
    if n==0: return 0
    if n==1: return k
    same=(k)*(1); diff=k*(k-1)
    for _ in range(2,n): same,diff=diff,(same+diff)*(k-1)
    return same+diff

def longest_valid_parens(s):
    stack=[-1]; best=0
    for i,c in enumerate(s):
        if c=='(': stack.append(i)
        else:
            stack.pop()
            if not stack: stack.append(i)
            else: best=max(best,i-stack[-1])
    return best

def can_reach_zero(lst,start):
    n=len(lst); visited=set()
    def dfs(i):
        if i<0 or i>=n or i in visited: return False
        if lst[i]==0: return True
        visited.add(i)
        return dfs(i+lst[i]) or dfs(i-lst[i])
    return dfs(start)

def tiling_ways(n):
    if n<=1: return 1
    a,b=1,1
    for _ in range(n-1): a,b=b,a+b
    return b

def min_cost_cuts(n,cuts):
    cuts=sorted([0]+cuts+[n]); m=len(cuts)
    dp=[[0]*m for _ in range(m)]
    for l in range(2,m):
        for i in range(m-l):
            j=i+l; dp[i][j]=float('inf')
            for k in range(i+1,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]+cuts[j]-cuts[i])
    return dp[0][m-1]
