# Day 24 — Array Problems — SOLUTIONS

def find_min_max(lst):
    mn=mx=lst[0]
    for x in lst[1:]:
        if x<mn: mn=x
        if x>mx: mx=x
    return (mn,mx)

def remove_duplicates(lst):
    if not lst: return 0
    k=1
    for i in range(1,len(lst)):
        if lst[i]!=lst[k-1]: lst[k]=lst[i]; k+=1
    return k

def two_sum(lst,target):
    seen={}
    for i,x in enumerate(lst):
        if target-x in seen: return (seen[target-x],i)
        seen[x]=i

def max_subarray(lst):
    curr=best=lst[0]
    for x in lst[1:]: curr=max(x,curr+x); best=max(best,curr)
    return best

def rotate(lst,k):
    n=len(lst); k=k%n
    return lst[-k:]+lst[:-k] if k else lst[:]

def product_except_self(lst):
    n=len(lst); result=[1]*n
    prefix=1
    for i in range(n): result[i]=prefix; prefix*=lst[i]
    suffix=1
    for i in range(n-1,-1,-1): result[i]*=suffix; suffix*=lst[i]
    return result

def lis_length(lst):
    if not lst: return 0
    dp=[1]*len(lst)
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[j]<lst[i]: dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

def merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0])
    merged=[intervals[0]]
    for start,end in intervals[1:]:
        if start<=merged[-1][1]: merged[-1][1]=max(merged[-1][1],end)
        else: merged.append([start,end])
    return merged
