# Day 33 — Dynamic Programming — SOLUTIONS

def climb_stairs(n):
    if n<=2: return n
    a,b=1,2
    for _ in range(n-2): a,b=b,a+b
    return b

def rob(houses):
    if not houses: return 0
    if len(houses)==1: return houses[0]
    prev2,prev1=0,0
    for h in houses: prev2,prev1=prev1,max(prev1,prev2+h)
    return prev1

def coin_change(coins,amount):
    dp=[float('inf')]*(amount+1); dp[0]=0
    for a in range(1,amount+1):
        for c in coins:
            if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

def lcs(s1,s2):
    m,n=len(s1),len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

def knapsack(weights,values,capacity):
    n=len(weights); dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(capacity+1):
            dp[i][w]=dp[i-1][w]
            if weights[i-1]<=w: dp[i][w]=max(dp[i][w],dp[i-1][w-weights[i-1]]+values[i-1])
    return dp[n][capacity]

def word_break(s,word_dict):
    words=set(word_dict); dp=[False]*(len(s)+1); dp[0]=True
    for i in range(1,len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in words: dp[i]=True; break
    return dp[len(s)]

def unique_paths(m,n):
    dp=[[1]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n): dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]

def max_product(lst):
    mn=mx=result=lst[0]
    for x in lst[1:]: mn,mx=min(x,mn*x,mx*x),max(x,mn*x,mx*x); result=max(result,mx)
    return result
