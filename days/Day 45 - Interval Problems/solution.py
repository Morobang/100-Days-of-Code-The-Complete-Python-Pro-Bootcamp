# Day 45 — Interval Problems — SOLUTIONS
import heapq

def merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0]); merged=[intervals[0][:]]
    for s,e in intervals[1:]:
        if s<=merged[-1][1]: merged[-1][1]=max(merged[-1][1],e)
        else: merged.append([s,e])
    return merged

def insert_interval(intervals,new):
    result=[]; i=0; n=len(intervals)
    while i<n and intervals[i][1]<new[0]: result.append(intervals[i]); i+=1
    while i<n and intervals[i][0]<=new[1]:
        new[0]=min(new[0],intervals[i][0]); new[1]=max(new[1],intervals[i][1]); i+=1
    result.append(new)
    while i<n: result.append(intervals[i]); i+=1
    return result

def can_attend(intervals):
    intervals.sort(); prev_end=float('-inf')
    for s,e in intervals:
        if s<prev_end: return False
        prev_end=e
    return True

def min_rooms(intervals):
    intervals.sort(key=lambda x:x[0]); heap=[]
    for s,e in intervals:
        if heap and heap[0]<=s: heapq.heapreplace(heap,e)
        else: heapq.heappush(heap,e)
    return len(heap)

def employee_free_time(schedules):
    all_intervals=sorted([iv for emp in schedules for iv in emp],key=lambda x:x[0])
    merged=merge_intervals(all_intervals); free=[]
    for i in range(1,len(merged)):
        if merged[i-1][1]<merged[i][0]: free.append([merged[i-1][1],merged[i][0]])
    return free

class RangeModule:
    def __init__(self): self.ranges=[]
    def add_range(self,l,r):
        new=[l,r]; tmp=[]
        for s,e in self.ranges:
            if e<l: tmp.append([s,e])
            elif s>r: tmp.append(new); new=None; tmp.append([s,e])
            else: new[0]=min(new[0],s); new[1]=max(new[1],e)
        if new: tmp.append(new)
        self.ranges=tmp
    def query_range(self,l,r):
        for s,e in self.ranges:
            if s<=l and e>=r: return True
        return False
    def remove_range(self,l,r):
        tmp=[]
        for s,e in self.ranges:
            if e<=l or s>=r: tmp.append([s,e])
            else:
                if s<l: tmp.append([s,l])
                if e>r: tmp.append([r,e])
        self.ranges=tmp

def count_overlapping(intervals):
    intervals.sort(); count=0; max_end=float('-inf')
    for s,e in intervals:
        if s<max_end: count+=1
        max_end=max(max_end,e)
    return count
