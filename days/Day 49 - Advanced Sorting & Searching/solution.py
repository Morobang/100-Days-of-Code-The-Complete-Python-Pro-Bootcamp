# Day 49 — Advanced Sorting — SOLUTIONS
import random, heapq
from collections import Counter

def kth_smallest(lst,k):
    pivot=random.choice(lst)
    low=[x for x in lst if x<pivot]
    mid=[x for x in lst if x==pivot]
    high=[x for x in lst if x>pivot]
    if k<len(low): return kth_smallest(low,k)
    elif k<len(low)+len(mid): return pivot
    else: return kth_smallest(high,k-len(low)-len(mid))

def counting_sort(lst):
    if not lst: return lst
    mn,mx=min(lst),max(lst); count=[0]*(mx-mn+1)
    for x in lst: count[x-mn]+=1
    return [i+mn for i,c in enumerate(count) for _ in range(c)]

def sort_colors(lst):
    lo=mid=0; hi=len(lst)-1
    while mid<=hi:
        if lst[mid]==0: lst[lo],lst[mid]=lst[mid],lst[lo]; lo+=1; mid+=1
        elif lst[mid]==1: mid+=1
        else: lst[mid],lst[hi]=lst[hi],lst[mid]; hi-=1

def sort_by_freq(s):
    return ''.join(c*f for c,f in Counter(s).most_common())

def wiggle_sort(lst):
    for i in range(1,len(lst)):
        if (i%2==1 and lst[i]<lst[i-1]) or (i%2==0 and lst[i]>lst[i-1]):
            lst[i],lst[i-1]=lst[i-1],lst[i]

def top_k_words(words,k):
    return [w for w,_ in sorted(Counter(words).items(),key=lambda x:(-x[1],x[0]))[:k]]

class KthLargest:
    def __init__(self,k,nums):
        self.k=k; self.heap=[]
        for n in nums: self.add(n)
    def add(self,val):
        heapq.heappush(self.heap,val)
        while len(self.heap)>self.k: heapq.heappop(self.heap)
        return self.heap[0]

def sort_k_sorted(lst,k):
    heap=lst[:k+1]; heapq.heapify(heap)
    result=[]
    for x in lst[k+1:]: result.append(heapq.heapreplace(heap,x))
    while heap: result.append(heapq.heappop(heap))
    return result
