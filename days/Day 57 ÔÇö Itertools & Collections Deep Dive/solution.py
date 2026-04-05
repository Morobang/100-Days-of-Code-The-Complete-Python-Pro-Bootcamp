# Day 57 — Itertools & Collections — SOLUTIONS
from itertools import accumulate, groupby, combinations
from collections import Counter, deque, defaultdict, OrderedDict, namedtuple
import re, operator

def running_stats(lst):
    return list(zip(
        accumulate(lst),
        accumulate(lst, min),
        accumulate(lst, max)
    ))

def sliding_window_avg(lst,k):
    d=deque(lst[:k]); total=sum(d); result=[total/k]
    for x in lst[k:]:
        total+=x-d.popleft(); d.append(x); result.append(total/k)
    return result

def top_words(text,n):
    words=re.findall(r"[a-z']+",text.lower())
    return Counter(words).most_common(n)

def group_consecutive(lst):
    return [(k,list(g)) for k,g in groupby(lst)]

def all_subsets(lst):
    return [list(c) for r in range(1,len(lst)+1) for c in combinations(lst,r)]

class LRUCache:
    def __init__(self,capacity): self.cap=capacity; self.cache=OrderedDict()
    def get(self,key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key); return self.cache[key]
    def put(self,key,value):
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache)>self.cap: self.cache.popitem(last=False)

GameRecord=namedtuple('GameRecord',['player','game','score','date'])

def build_registry(records):
    reg=defaultdict(list)
    for r in records: reg[r.player].append(r)
    return dict(reg)
