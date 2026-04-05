# Day 59 — Hard Problems I — SOLUTIONS
import heapq
from collections import defaultdict, deque

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

def trap(heights):
    l,r=0,len(heights)-1; lmax=rmax=water=0
    while l<=r:
        if heights[l]<=heights[r]:
            if heights[l]>=lmax: lmax=heights[l]
            else: water+=lmax-heights[l]
            l+=1
        else:
            if heights[r]>=rmax: rmax=heights[r]
            else: water+=rmax-heights[r]
            r-=1
    return water

def largest_rectangle(heights):
    stack=[]; max_area=0; heights=heights+[0]
    for i,h in enumerate(heights):
        start=i
        while stack and stack[-1][1]>h:
            idx,hgt=stack.pop(); max_area=max(max_area,(i-idx)*hgt); start=idx
        stack.append((start,h))
    return max_area

class TreeNode:
    def __init__(self,v): self.val=v; self.left=self.right=None

def serialize(root):
    vals=[]; 
    def pre(node):
        if not node: vals.append('#'); return
        vals.append(str(node.val)); pre(node.left); pre(node.right)
    pre(root); return ','.join(vals)

def deserialize(data):
    it=iter(data.split(','))
    def build():
        v=next(it)
        if v=='#': return None
        node=TreeNode(int(v)); node.left=build(); node.right=build(); return node
    return build()

def word_ladder(begin,end,word_list):
    words=set(word_list)
    if end not in words: return 0
    q=deque([(begin,1)])
    while q:
        word,dist=q.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nw=word[:i]+c+word[i+1:]
                if nw==end: return dist+1
                if nw in words: words.discard(nw); q.append((nw,dist+1))
    return 0

def alien_order(words):
    chars={c for w in words for c in w}
    graph=defaultdict(set); indegree={c:0 for c in chars}
    for i in range(len(words)-1):
        a,b=words[i],words[i+1]
        if len(a)>len(b) and a.startswith(b): return ''
        for c1,c2 in zip(a,b):
            if c1!=c2 and c2 not in graph[c1]:
                graph[c1].add(c2); indegree[c2]+=1; break
    q=deque([c for c in chars if indegree[c]==0]); result=''
    while q:
        c=q.popleft(); result+=c
        for n in graph[c]:
            indegree[n]-=1
            if indegree[n]==0: q.append(n)
    return result if len(result)==len(chars) else ''

def max_profit_cooldown(prices):
    if len(prices)<2: return 0
    hold=sold=rest=float('-inf'),float('-inf'),0
    hold,sold,rest=-prices[0],float('-inf'),0
    for p in prices[1:]:
        hold,sold,rest=max(hold,rest-p),hold+p,max(rest,sold)
    return max(sold,rest)

def min_window(s,t):
    need=defaultdict(int)
    for c in t: need[c]+=1
    missing=len(t); l=0; best=''
    for r,c in enumerate(s):
        if need[c]>0: missing-=1
        need[c]-=1
        if missing==0:
            while need[s[l]]<0: need[s[l]]+=1; l+=1
            if not best or r-l+1<len(best): best=s[l:r+1]
            need[s[l]]+=1; missing+=1; l+=1
    return best
