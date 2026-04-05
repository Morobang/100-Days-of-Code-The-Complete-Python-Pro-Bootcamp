# Day 80 — Hard Problems IV — SOLUTIONS
import heapq
from functools import cmp_to_key

def min_arrows(points):
    points.sort(key=lambda x:x[1]); arrows=0; end=float('-inf')
    for s,e in points:
        if s>end: arrows+=1; end=e
    return arrows

def calculate(s):
    stack=[]; num=0; op='+'
    s=s.strip()+'+'
    for c in s:
        if c.isdigit(): num=num*10+int(c)
        elif c in '+-*/':
            if op=='+': stack.append(num)
            elif op=='-': stack.append(-num)
            elif op=='*': stack.append(stack.pop()*num)
            elif op=='/': stack.append(int(stack.pop()/num))
            op=c; num=0
    return sum(stack)

class Node:
    def __init__(self,v,nxt=None,rand=None): self.val=v; self.next=nxt; self.random=rand

def copy_random_list(head):
    if not head: return None
    mapping={}; cur=head
    while cur: mapping[cur]=Node(cur.val); cur=cur.next
    cur=head
    while cur:
        if cur.next: mapping[cur].next=mapping[cur.next]
        if cur.random: mapping[cur].random=mapping[cur.random]
        cur=cur.next
    return mapping[head]

def swim_in_water(grid):
    n=len(grid); heap=[(grid[0][0],0,0)]; visited=set([(0,0)])
    while heap:
        t,r,c=heapq.heappop(heap)
        if r==n-1 and c==n-1: return t
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                visited.add((nr,nc)); heapq.heappush(heap,(max(t,grid[nr][nc]),nr,nc))

def strange_printer(s):
    n=len(s); dp=[[0]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        dp[i][i]=1
        for j in range(i+1,n):
            dp[i][j]=dp[i][j-1]+1
            for k in range(i,j):
                if s[k]==s[j]: dp[i][j]=min(dp[i][j],(dp[i][k-1] if k>i else 0)+dp[k][j-1] if j>k else (dp[i][k-1] if k>i else 0))
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            dp[i][j]=dp[i+1][j]+1 if True else dp[i][j]
    # Simpler DP
    dp2=[[0]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        dp2[i][i]=1
        for j in range(i+1,n):
            dp2[i][j]=dp2[i][j-1]+1
            for k in range(i,j):
                if s[k]==s[j]:
                    extra=dp2[i][k-1] if k>i else 0
                    dp2[i][j]=min(dp2[i][j],extra+dp2[k][j-1])
    return dp2[0][n-1]

def min_interval(intervals,queries):
    intervals.sort(); sorted_q=sorted(enumerate(queries),key=lambda x:x[1])
    result=[-1]*len(queries); heap=[]; i=0
    for idx,q in sorted_q:
        while i<len(intervals) and intervals[i][0]<=q:
            s,e=intervals[i]; heapq.heappush(heap,(e-s+1,e)); i+=1
        while heap and heap[0][1]<q: heapq.heappop(heap)
        if heap: result[idx]=heap[0][0]
    return result

class MedianFinder:
    def __init__(self): self.low=[]; self.high=[]
    def add_num(self,num):
        heapq.heappush(self.low,-num)
        heapq.heappush(self.high,-heapq.heappop(self.low))
        if len(self.high)>len(self.low): heapq.heappush(self.low,-heapq.heappop(self.high))
    def find_median(self):
        if len(self.low)>len(self.high): return float(-self.low[0])
        return (-self.low[0]+self.high[0])/2.0

def largest_number(nums):
    def cmp(a,b):
        if a+b>b+a: return -1
        elif a+b<b+a: return 1
        return 0
    strs=[str(n) for n in nums]
    strs.sort(key=cmp_to_key(cmp))
    result=''.join(strs)
    return '0' if result[0]=='0' else result
