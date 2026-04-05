# Day 34 — Two Pointers & Sliding Window — SOLUTIONS
from collections import defaultdict

def two_sum_sorted(lst,target):
    l,r=0,len(lst)-1
    while l<r:
        s=lst[l]+lst[r]
        if s==target: return (l,r)
        elif s<target: l+=1
        else: r-=1

def three_sum(lst):
    lst.sort(); result=[]
    for i in range(len(lst)-2):
        if i>0 and lst[i]==lst[i-1]: continue
        l,r=i+1,len(lst)-1
        while l<r:
            s=lst[i]+lst[l]+lst[r]
            if s==0: result.append([lst[i],lst[l],lst[r]]); l+=1; r-=1
            elif s<0: l+=1
            else: r-=1
    return result

def max_water(heights):
    l,r=0,len(heights)-1; best=0
    while l<r:
        best=max(best,min(heights[l],heights[r])*(r-l))
        if heights[l]<heights[r]: l+=1
        else: r-=1
    return best

def min_window(s,t):
    need=defaultdict(int)
    for c in t: need[c]+=1
    missing=len(t); l=0; best=''
    for r,c in enumerate(s):
        if need[c]>0: missing-=1
        need[c]-=1
        if missing==0:
            while need[s[l]]<0: need[s[l]]+=1; l+=1
            if not best or r-l+1<len(best): best=s[l:r+1]
            need[s[l]]+=1; missing+=1; l+=1
    return best

def longest_k_distinct(s,k):
    counts=defaultdict(int); l=best=0
    for r,c in enumerate(s):
        counts[c]+=1
        while len(counts)>k: counts[s[l]]-=1; (counts.pop(s[l]) if counts[s[l]]==0 else None); l+=1
        best=max(best,r-l+1)
    return best

def remove_dups_ii(lst):
    k=0
    for n in lst:
        if k<2 or lst[k-2]!=n: lst[k]=n; k+=1
    return k

def trap(heights):
    l,r=0,len(heights)-1; lmax=rmax=water=0
    while l<=r:
        if heights[l]<=heights[r]:
            if heights[l]>=lmax: lmax=heights[l]
            else: water+=lmax-heights[l]
            l+=1
        else:
            if heights[r]>=rmax: rmax=heights[r]
            else: water+=rmax-heights[r]
            r-=1
    return water

def total_fruit(fruits):
    counts=defaultdict(int); l=best=0
    for r,f in enumerate(fruits):
        counts[f]+=1
        while len(counts)>2: counts[fruits[l]]-=1; (counts.pop(fruits[l]) if counts[fruits[l]]==0 else None); l+=1
        best=max(best,r-l+1)
    return best
