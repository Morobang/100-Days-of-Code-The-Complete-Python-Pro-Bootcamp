# Day 32 — Stacks & Queues — SOLUTIONS
from collections import deque

def is_valid(s):
    stack=[]; pairs={')':'(',']':'[','}':'{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1]!=pairs[c]: return False
            stack.pop()
    return not stack

class MinStack:
    def __init__(self): self._data=[]; self._mins=[]
    def push(self,val):
        self._data.append(val)
        self._mins.append(min(val,self._mins[-1] if self._mins else val))
    def pop(self): self._data.pop(); self._mins.pop()
    def get_min(self): return self._mins[-1]

def eval_rpn(tokens):
    stack=[]
    ops={'+':lambda a,b:a+b,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:int(a/b)}
    for t in tokens:
        if t in ops: b,a=stack.pop(),stack.pop(); stack.append(ops[t](a,b))
        else: stack.append(int(t))
    return stack[0]

def daily_temps(temps):
    result=[0]*len(temps); stack=[]
    for i,t in enumerate(temps):
        while stack and temps[stack[-1]]<t:
            j=stack.pop(); result[j]=i-j
        stack.append(i)
    return result

def sliding_max(lst,k):
    dq=deque(); result=[]
    for i,v in enumerate(lst):
        while dq and lst[dq[-1]]<v: dq.pop()
        dq.append(i)
        if dq[0]==i-k: dq.popleft()
        if i>=k-1: result.append(lst[dq[0]])
    return result

def largest_rectangle(heights):
    stack=[]; max_area=0; heights=heights+[0]
    for i,h in enumerate(heights):
        start=i
        while stack and stack[-1][1]>h:
            idx,hgt=stack.pop(); max_area=max(max_area,(i-idx)*hgt); start=idx
        stack.append((start,h))
    return max_area

def decode_string(s):
    stack=[]; cur=''; k=0
    for c in s:
        if c.isdigit(): k=k*10+int(c)
        elif c=='[': stack.append((cur,k)); cur=''; k=0
        elif c==']': prev,n=stack.pop(); cur=prev+cur*n
        else: cur+=c
    return cur

def shortest_path(grid,start,end):
    rows,cols=len(grid),len(grid[0])
    q=deque([(start,0)]); visited={start}
    while q:
        (r,c),dist=q.popleft()
        if (r,c)==end: return dist
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0 and (nr,nc) not in visited:
                visited.add((nr,nc)); q.append(((nr,nc),dist+1))
    return -1
