# Day 38 — Binary Search — SOLUTIONS
import math

def binary_search(lst,target):
    lo,hi=0,len(lst)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if lst[mid]==target: return mid
        elif lst[mid]<target: lo=mid+1
        else: hi=mid-1
    return -1

def search_range(lst,target):
    def find(go_left):
        lo,hi,result=0,len(lst)-1,-1
        while lo<=hi:
            mid=(lo+hi)//2
            if lst[mid]==target:
                result=mid
                if go_left: hi=mid-1
                else: lo=mid+1
            elif lst[mid]<target: lo=mid+1
            else: hi=mid-1
        return result
    return (find(True),find(False))

def search_rotated(lst,target):
    lo,hi=0,len(lst)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if lst[mid]==target: return mid
        if lst[lo]<=lst[mid]:
            if lst[lo]<=target<lst[mid]: hi=mid-1
            else: lo=mid+1
        else:
            if lst[mid]<target<=lst[hi]: lo=mid+1
            else: hi=mid-1
    return -1

def find_min_rotated(lst):
    lo,hi=0,len(lst)-1
    while lo<hi:
        mid=(lo+hi)//2
        if lst[mid]>lst[hi]: lo=mid+1
        else: hi=mid
    return lst[lo]

def guess_game(secret,n):
    lo,hi=1,n; guesses=0
    while lo<=hi:
        mid=(lo+hi)//2; guesses+=1
        if mid==secret: return guesses
        elif mid<secret: lo=mid+1
        else: hi=mid-1
    return guesses

def find_peak(lst):
    lo,hi=0,len(lst)-1
    while lo<hi:
        mid=(lo+hi)//2
        if lst[mid]>lst[mid+1]: hi=mid
        else: lo=mid+1
    return lo

def median_sorted_arrays(a,b):
    if len(a)>len(b): return median_sorted_arrays(b,a)
    m,n=len(a),len(b); lo,hi=0,m
    while lo<=hi:
        pm=(lo+hi)//2; pn=(m+n+1)//2-pm
        lmax_a=float('-inf') if pm==0 else a[pm-1]
        rmin_a=float('inf') if pm==m else a[pm]
        lmax_b=float('-inf') if pn==0 else b[pn-1]
        rmin_b=float('inf') if pn==n else b[pn]
        if lmax_a<=rmin_b and lmax_b<=rmin_a:
            if (m+n)%2: return float(max(lmax_a,lmax_b))
            return (max(lmax_a,lmax_b)+min(rmin_a,rmin_b))/2
        elif lmax_a>rmin_b: hi=pm-1
        else: lo=pm+1

def min_eating_speed(piles,h):
    lo,hi=1,max(piles)
    while lo<hi:
        mid=(lo+hi)//2
        if sum(math.ceil(p/mid) for p in piles)<=h: hi=mid
        else: lo=mid+1
    return lo
