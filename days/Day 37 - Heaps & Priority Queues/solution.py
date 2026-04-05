# Day 37 — Heaps — SOLUTIONS
import heapq
from collections import Counter

def kth_largest(lst,k):
    heap=[]
    for n in lst:
        heapq.heappush(heap,n)
        if len(heap)>k: heapq.heappop(heap)
    return heap[0]

def kth_smallest(lst,k):
    return heapq.nsmallest(k,lst)[-1]

def k_closest(points,k):
    return heapq.nsmallest(k,points,key=lambda p:p[0]**2+p[1]**2)

def top_k_frequent(lst,k):
    return [x for x,_ in Counter(lst).most_common(k)]

def merge_k_sorted(lists):
    heap=[]; result=[]
    for i,l in enumerate(lists):
        if l: heapq.heappush(heap,(l[0],i,0))
    while heap:
        val,i,j=heapq.heappop(heap); result.append(val)
        if j+1<len(lists[i]): heapq.heappush(heap,(lists[i][j+1],i,j+1))
    return result

class MedianFinder:
    def __init__(self): self.low=[]; self.high=[]
    def add_num(self,num):
        heapq.heappush(self.low,-num)
        heapq.heappush(self.high,-heapq.heappop(self.low))
        if len(self.high)>len(self.low):
            heapq.heappush(self.low,-heapq.heappop(self.high))
    def find_median(self):
        if len(self.low)>len(self.high): return float(-self.low[0])
        return (-self.low[0]+self.high[0])/2.0

def least_interval(tasks,n):
    counts=list(Counter(tasks).values())
    max_count=max(counts)
    max_count_tasks=counts.count(max_count)
    return max((max_count-1)*(n+1)+max_count_tasks,len(tasks))
