# Day 71 — Divide and Conquer — SOLUTIONS
import math

def fast_pow(base,exp):
    if exp==0: return 1
    half=fast_pow(base,exp//2)
    return half*half if exp%2==0 else half*half*base

def count_inversions(lst):
    if len(lst)<=1: return 0,lst
    mid=len(lst)//2
    lc,left=count_inversions(lst[:mid])
    rc,right=count_inversions(lst[mid:])
    merged=[]; inv=0; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: merged.append(left[i]); i+=1
        else: merged.append(right[j]); inv+=len(left)-i; j+=1
    merged+=left[i:]+right[j:]
    return lc+rc+inv,merged
count_inversions=lambda lst:__count_inv(lst)[0]
def __count_inv(lst):
    if len(lst)<=1: return 0,lst
    mid=len(lst)//2
    lc,left=__count_inv(lst[:mid]); rc,right=__count_inv(lst[mid:])
    merged=[]; inv=0; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: merged.append(left[i]); i+=1
        else: merged.append(right[j]); inv+=len(left)-i; j+=1
    merged+=left[i:]+right[j:]; return lc+rc+inv,merged
count_inversions=lambda lst:__count_inv(lst)[0]

def closest_pair(points):
    def dist(p1,p2): return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    def bf(pts): return min(dist(pts[i],pts[j]) for i in range(len(pts)) for j in range(i+1,len(pts)))
    def strip_closest(strip,d):
        strip.sort(key=lambda p:p[1]); mn=d
        for i in range(len(strip)):
            j=i+1
            while j<len(strip) and strip[j][1]-strip[i][1]<mn: mn=min(mn,dist(strip[i],strip[j])); j+=1
        return mn
    def rec(pts):
        if len(pts)<=3: return bf(pts)
        mid=len(pts)//2; mx=pts[mid][0]
        dl=rec(pts[:mid]); dr=rec(pts[mid:]); d=min(dl,dr)
        strip=[p for p in pts if abs(p[0]-mx)<d]
        return min(d,strip_closest(strip,d))
    pts=sorted(points); return rec(pts)

def max_subarray_dc(lst):
    def helper(l,r):
        if l==r: return lst[l]
        mid=(l+r)//2
        ls=rs=cs=0; mn=float('-inf')
        for i in range(mid,l-1,-1): cs+=lst[i]; mn=max(mn,cs)
        left_cross=mn; mn=float('-inf'); cs=0
        for i in range(mid+1,r+1): cs+=lst[i]; mn=max(mn,cs)
        right_cross=mn
        return max(helper(l,mid),helper(mid+1,r),left_cross+right_cross)
    return helper(0,len(lst)-1)

def kth_smallest(lst,k):
    pivot=lst[len(lst)//2]
    lo=[x for x in lst if x<pivot]
    mi=[x for x in lst if x==pivot]
    hi=[x for x in lst if x>pivot]
    if k<=len(lo): return kth_smallest(lo,k)
    if k<=len(lo)+len(mi): return pivot
    return kth_smallest(hi,k-len(lo)-len(mi))

def karatsuba(x,y):
    if x<10 or y<10: return x*y
    n=max(len(str(x)),len(str(y))); m=n//2
    hi1,lo1=divmod(x,10**m); hi2,lo2=divmod(y,10**m)
    z0=karatsuba(lo1,lo2); z2=karatsuba(hi1,hi2)
    z1=karatsuba(lo1+hi1,lo2+hi2)-z2-z0
    return z2*10**(2*m)+z1*10**m+z0

def get_skyline(buildings):
    import heapq
    events=[]
    for l,r,h in buildings: events.append((l,-h,r)); events.append((r,0,0))
    events.sort(); heap=[(0,float('inf'))]; result=[]; prev=0
    for x,nh,r in events:
        if nh!=0: heapq.heappush(heap,(nh,r))
        while heap[0][1]<=x: heapq.heappop(heap)
        curr=-heap[0][0]
        if curr!=prev: result.append([x,curr]); prev=curr
    return result

def merge_k_arrays(arrays):
    arrays=[a for a in arrays if a]
    if not arrays: return []
    if len(arrays)==1: return arrays[0]
    mid=len(arrays)//2
    left=merge_k_arrays(arrays[:mid]); right=merge_k_arrays(arrays[mid:])
    result=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: result.append(left[i]); i+=1
        else: result.append(right[j]); j+=1
    return result+left[i:]+right[j:]
