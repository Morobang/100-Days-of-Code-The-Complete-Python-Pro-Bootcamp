# Day 47 — Advanced Hashing — SOLUTIONS
from collections import defaultdict, Counter
from math import gcd

def group_anagrams(words):
    groups=defaultdict(list)
    for w in words: groups[tuple(sorted(w))].append(w)
    return list(groups.values())

def is_isomorphic(s,t):
    return len(set(zip(s,t)))==len(set(s))==len(set(t))

def word_pattern(pattern,s):
    words=s.split()
    if len(pattern)!=len(words): return False
    return len(set(zip(pattern,words)))==len(set(pattern))==len(set(words))

def max_equal_01(lst):
    seen={0:-1}; prefix=best=0
    for i,v in enumerate(lst):
        prefix+=(1 if v==1 else -1)
        if prefix in seen: best=max(best,i-seen[prefix])
        else: seen[prefix]=i
    return best

def longest_arith_seq(lst):
    dp=[{} for _ in lst]; best=2
    for i in range(1,len(lst)):
        for j in range(i):
            d=lst[i]-lst[j]
            dp[i][d]=dp[j].get(d,1)+1
            best=max(best,dp[i][d])
    return best

def subarray_sum_count(lst,k):
    count=prefix=0; seen={0:1}
    for x in lst:
        prefix+=x; count+=seen.get(prefix-k,0)
        seen[prefix]=seen.get(prefix,0)+1
    return count

def least_bricks(wall):
    edges=Counter()
    for row in wall:
        pos=0
        for brick in row[:-1]: pos+=brick; edges[pos]+=1
    return len(wall)-max(edges.values(),default=0)

def max_points(points):
    if len(points)<=2: return len(points)
    best=2
    for i,p1 in enumerate(points):
        slopes=defaultdict(int)
        for j,p2 in enumerate(points):
            if i==j: continue
            dy,dx=p2[1]-p1[1],p2[0]-p1[0]
            g=gcd(abs(dy),abs(dx)) or 1
            slope=(dy//g,dx//g)
            if dx==0: slope=('inf',0)
            elif dy==0: slope=(0,'inf')
            else:
                if dx<0: dy,dx=-dy,-dx
            slopes[(dy//g if dx else dy,dx//g if dy else dx)]+=1
        best=max(best,max(slopes.values())+1)
    return best
