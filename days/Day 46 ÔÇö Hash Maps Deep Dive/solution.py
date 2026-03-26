# Day 46 — Hash Maps Deep Dive — SOLUTIONS
from collections import OrderedDict, Counter

class MyHashMap:
    def __init__(self): self.capacity=1000; self.b=[[] for _ in range(self.capacity)]
    def _h(self,k): return k%self.capacity
    def put(self,k,v):
        for i,(ek,ev) in enumerate(self.b[self._h(k)]):
            if ek==k: self.b[self._h(k)][i]=(k,v); return
        self.b[self._h(k)].append((k,v))
    def get(self,k):
        for ek,ev in self.b[self._h(k)]:
            if ek==k: return ev
        return -1
    def remove(self,k):
        self.b[self._h(k)]=[(ek,ev) for ek,ev in self.b[self._h(k)] if ek!=k]

class MyHashSet:
    def __init__(self): self.capacity=1000; self.b=[[] for _ in range(self.capacity)]
    def _h(self,k): return k%self.capacity
    def add(self,k):
        if not self.contains(k): self.b[self._h(k)].append(k)
    def contains(self,k): return k in self.b[self._h(k)]
    def remove(self,k): self.b[self._h(k)]=[x for x in self.b[self._h(k)] if x!=k]

class LRUCache:
    def __init__(self,cap): self.cap=cap; self.cache=OrderedDict()
    def get(self,k):
        if k not in self.cache: return -1
        self.cache.move_to_end(k); return self.cache[k]
    def put(self,k,v):
        if k in self.cache: self.cache.move_to_end(k)
        self.cache[k]=v
        if len(self.cache)>self.cap: self.cache.popitem(last=False)

def is_isomorphic(s,t):
    return len(set(zip(s,t)))==len(set(s))==len(set(t))

def word_pattern(pattern,s):
    words=s.split()
    if len(pattern)!=len(words): return False
    return len(set(zip(pattern,words)))==len(set(pattern))==len(set(words))

def longest_consecutive(lst):
    s=set(lst); best=0
    for x in s:
        if x-1 not in s:
            length=1
            while x+length in s: length+=1
            best=max(best,length)
    return best

def can_construct(ransom,magazine):
    mag=Counter(magazine)
    for c in ransom:
        mag[c]-=1
        if mag[c]<0: return False
    return True

def subarray_sum(lst,k):
    count=0; prefix=0; seen={0:1}
    for x in lst:
        prefix+=x; count+=seen.get(prefix-k,0); seen[prefix]=seen.get(prefix,0)+1
    return count
