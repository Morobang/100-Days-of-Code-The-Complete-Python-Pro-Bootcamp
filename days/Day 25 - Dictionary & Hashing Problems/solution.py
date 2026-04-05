# Day 25 — Hashing Problems — SOLUTIONS
from collections import Counter, defaultdict

def most_common(lst): return Counter(lst).most_common(1)[0][0]

def two_sum_values(lst,target):
    seen=set()
    for x in lst:
        if target-x in seen: return (target-x,x)
        seen.add(x)
    return None

def subarray_sum_count(lst,k):
    count=0; prefix=0; seen={0:1}
    for x in lst:
        prefix+=x; count+=seen.get(prefix-k,0)
        seen[prefix]=seen.get(prefix,0)+1
    return count

def first_duplicate(lst):
    seen=set()
    for x in lst:
        if x in seen: return x
        seen.add(x)
    return None

def intersection(a,b): return list(set(a)&set(b))

def longest_consecutive(lst):
    s=set(lst); best=0
    for x in s:
        if x-1 not in s:
            length=1
            while x+length in s: length+=1
            best=max(best,length)
    return best

def four_sum_count(a,b,c,d):
    ab=Counter(x+y for x in a for y in b)
    return sum(ab.get(-(x+y),0) for x in c for y in d)

def min_window(s,t):
    need=Counter(t); missing=len(t)
    best=float('inf'),0,0; lo=0
    for hi,c in enumerate(s,1):
        if need[c]>0: missing-=1
        need[c]-=1
        if not missing:
            while need[s[lo]]<0: need[s[lo]]+=1; lo+=1
            if hi-lo<best[0]: best=hi-lo,lo,hi
            need[s[lo]]+=1; missing+=1; lo+=1
    return s[best[1]:best[2]] if best[0]!=float('inf') else ''
