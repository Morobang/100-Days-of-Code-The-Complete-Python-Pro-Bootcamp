# Day 44 — Greedy — SOLUTIONS

def can_jump(nums):
    reach=0
    for i,n in enumerate(nums):
        if i>reach: return False
        reach=max(reach,i+n)
    return True

def min_jumps(nums):
    jumps=curr_end=farthest=0
    for i in range(len(nums)-1):
        farthest=max(farthest,i+nums[i])
        if i==curr_end: jumps+=1; curr_end=farthest
    return jumps

def can_complete_circuit(gas,cost):
    total=tank=start=0
    for i in range(len(gas)):
        diff=gas[i]-cost[i]; total+=diff; tank+=diff
        if tank<0: start=i+1; tank=0
    return start if total>=0 else -1

def assign_cookies(children,cookies):
    children.sort(); cookies.sort()
    i=j=0
    while i<len(children) and j<len(cookies):
        if cookies[j]>=children[i]: i+=1
        j+=1
    return i

def erase_overlap(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x:x[1]); removed=0; end=intervals[0][1]
    for s,e in intervals[1:]:
        if s<end: removed+=1
        else: end=e
    return removed

def partition_labels(s):
    last={c:i for i,c in enumerate(s)}
    result=[]; start=anchor=0
    for i,c in enumerate(s):
        anchor=max(anchor,last[c])
        if i==anchor: result.append(i-start+1); start=i+1
    return result

def reconstruct_queue(people):
    people.sort(key=lambda p:(-p[0],p[1]))
    result=[]
    for p in people: result.insert(p[1],p)
    return result

def min_arrows(points):
    if not points: return 0
    points.sort(key=lambda x:x[1]); arrows=1; end=points[0][1]
    for s,e in points[1:]:
        if s>end: arrows+=1; end=e
    return arrows
