# Day 50 — Medium Problems — SOLUTIONS
from collections import defaultdict
import bisect, heapq

def length_of_longest(s):
    seen={}; best=lo=0
    for hi,c in enumerate(s):
        if c in seen and seen[c]>=lo: lo=seen[c]+1
        seen[c]=hi; best=max(best,hi-lo+1)
    return best

def max_water(heights):
    l,r=0,len(heights)-1; best=0
    while l<r:
        best=max(best,min(heights[l],heights[r])*(r-l))
        if heights[l]<heights[r]: l+=1
        else: r-=1
    return best

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

def coin_change(coins,amount):
    dp=[float('inf')]*(amount+1); dp[0]=0
    for a in range(1,amount+1):
        for c in coins:
            if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

class KthLargest:
    def __init__(self,k,initial):
        self.k=k; self.heap=[]
        for v in initial: self.add(v)
    def add(self,val):
        heapq.heappush(self.heap,val)
        while len(self.heap)>self.k: heapq.heappop(self.heap)
        return self.heap[0]

class Node:
    def __init__(self,v): self.val=v; self.next=None

def reorder_list(head):
    if not head: return
    slow=fast=head
    while fast and fast.next: slow=slow.next; fast=fast.next.next
    prev,cur=None,slow.next; slow.next=None
    while cur: nxt=cur.next; cur.next=prev; prev,cur=cur,nxt
    l1,l2=head,prev
    while l2: nxt1=l1.next; nxt2=l2.next; l1.next=l2; l2.next=nxt1; l1,l2=nxt1,nxt2

def find_duplicates(lst):
    result=[]
    for n in lst:
        idx=abs(n)-1
        if lst[idx]<0: result.append(abs(n))
        else: lst[idx]=-lst[idx]
    return result

def num_islands(grid):
    if not grid: return 0
    rows,cols=len(grid),len(grid[0]); count=0
    def dfs(r,c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1': return
        grid[r][c]='0'
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]: dfs(r+dr,c+dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1': dfs(r,c); count+=1
    return count

def decode_string(s):
    stack=[]; cur=''; k=0
    for c in s:
        if c.isdigit(): k=k*10+int(c)
        elif c=='[': stack.append((cur,k)); cur=''; k=0
        elif c==']': prev,n=stack.pop(); cur=prev+cur*n
        else: cur+=c
    return cur

class TimeMap:
    def __init__(self): self.store=defaultdict(list)
    def set(self,key,value,timestamp): self.store[key].append((timestamp,value))
    def get(self,key,timestamp):
        if key not in self.store: return ''
        times,vals=zip(*self.store[key])
        idx=bisect.bisect_right(times,timestamp)-1
        return vals[idx] if idx>=0 else ''
