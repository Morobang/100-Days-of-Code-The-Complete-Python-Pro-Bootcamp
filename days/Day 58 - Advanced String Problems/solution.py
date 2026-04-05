# Day 58 — Advanced Strings — SOLUTIONS
from functools import lru_cache

def longest_palindrome(s):
    def expand(l,r):
        while l>=0 and r<len(s) and s[l]==s[r]: l-=1; r+=1
        return s[l+1:r]
    best=''
    for i in range(len(s)):
        for p in (expand(i,i), expand(i,i+1)):
            if len(p)>len(best): best=p
    return best

def edit_distance(s1,s2):
    m,n=len(s1),len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=i
    for j in range(n+1): dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]: dp[i][j]=dp[i-1][j-1]
            else: dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]

def wildcard_match(s,p):
    m,n=len(s),len(p)
    dp=[[False]*(n+1) for _ in range(m+1)]; dp[0][0]=True
    for j in range(1,n+1): dp[0][j]=dp[0][j-1] and p[j-1]=='*'
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1]=='*': dp[i][j]=dp[i-1][j] or dp[i][j-1]
            elif p[j-1]=='?' or s[i-1]==p[j-1]: dp[i][j]=dp[i-1][j-1]
    return dp[m][n]

def lps(s):
    n=len(s); dp=[[0]*n for _ in range(n)]
    for i in range(n): dp[i][i]=1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if s[i]==s[j] and l==2: dp[i][j]=2
            elif s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
            else: dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]

def shortest_palindrome(s):
    t=s+'#'+s[::-1]
    fail=[0]*len(t); j=0
    for i in range(1,len(t)):
        while j and t[i]!=t[j]: j=fail[j-1]
        if t[i]==t[j]: j+=1
        fail[i]=j
    return s[fail[-1]:][::-1]+s

def count_subsequences(s,t):
    m,n=len(s),len(t)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j]+(dp[i-1][j-1] if s[i-1]==t[j-1] else 0)
    return dp[m][n]

def is_interleave(s1,s2,s3):
    m,n=len(s1),len(s2)
    if m+n!=len(s3): return False
    dp=[[False]*(n+1) for _ in range(m+1)]; dp[0][0]=True
    for i in range(1,m+1): dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
    for j in range(1,n+1): dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
    return dp[m][n]

@lru_cache(maxsize=None)
def is_scramble(s1,s2):
    if s1==s2: return True
    if sorted(s1)!=sorted(s2): return False
    n=len(s1)
    for i in range(1,n):
        if (is_scramble(s1[:i],s2[:i]) and is_scramble(s1[i:],s2[i:])) or            (is_scramble(s1[:i],s2[n-i:]) and is_scramble(s1[i:],s2[:n-i])):
            return True
    return False
