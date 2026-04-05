# Day 46 — Interval Problems — SOLUTIONS
import heapq

def merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0])
    merged=[intervals[0]]
    for s,e in intervals[1:]:
        if s<=merged[-1][1]: merged[-1][1]=max(merged[-1][1],e)
        else: merged.append([s,e])
    return merged

def insert_interval(intervals,new):
    result=[]; i=0
    while i<len(intervals) and intervals[i][1]<new[0]: result.append(intervals[i]); i+=1
    while i<len(intervals) and intervals[i][0]<=new[1]:
        new=[min(new[0],intervals[i][0]),max(new[1],intervals[i][1])]; i+=1
    result.append(new); result+=intervals[i:]; return result

def interval_intersection(a,b):
    result=[]; i=j=0
    while i<len(a) and j<len(b):
        lo=max(a[i][0],b[j][0]); hi=min(a[i][1],b[j][1])
        if lo<=hi: result.append([lo,hi])
        if a[i][1]<b[j][1]: i+=1
        else: j+=1
    return result

def count_non_overlapping(intervals):
    intervals.sort(key=lambda x:x[1]); count=0; last=float('-inf')
    for s,e in intervals:
        if s>=last: count+=1; last=e
    return count

def free_slots(busy_times,day_start,day_end):
    busy_times.sort(); slots=[]; prev=day_start
    for s,e in busy_times:
        if prev<s: slots.append([prev,s])
        prev=max(prev,e)
    if prev<day_end: slots.append([prev,day_end])
    return slots

def employee_free_time(schedules):
    all_intervals=sorted([iv for emp in schedules for iv in emp],key=lambda x:x[0])
    free=[]; prev_end=all_intervals[0][1]
    for s,e in all_intervals[1:]:
        if s>prev_end: free.append([prev_end,s])
        prev_end=max(prev_end,e)
    return free

def min_interval(intervals,queries):
    intervals.sort(); sorted_q=sorted(enumerate(queries),key=lambda x:x[1])
    result=[-1]*len(queries); heap=[]; i=0
    for idx,q in sorted_q:
        while i<len(intervals) and intervals[i][0]<=q:
            s,e=intervals[i]; heapq.heappush(heap,(e-s+1,e)); i+=1
        while heap and heap[0][1]<q: heapq.heappop(heap)
        if heap: result[idx]=heap[0][0]
    return result
