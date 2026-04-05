# Day 74 — System Design — SOLUTIONS
from collections import OrderedDict, defaultdict, deque
import time

class LRUCache:
    def __init__(self,capacity): self.cap=capacity; self.cache=OrderedDict()
    def get(self,key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key); return self.cache[key]
    def put(self,key,value):
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache)>self.cap: self.cache.popitem(last=False)

class RateLimiter:
    def __init__(self,rate,capacity):
        self.rate=rate; self.capacity=capacity
        self.tokens=capacity; self.last=time.time()
    def allow(self):
        now=time.time()
        self.tokens=min(self.capacity,self.tokens+(now-self.last)*self.rate)
        self.last=now
        if self.tokens>=1: self.tokens-=1; return True
        return False

class SlidingWindowLimiter:
    def __init__(self,max_requests,window_seconds):
        self.max=max_requests; self.window=window_seconds; self.times=deque()
    def allow(self):
        now=time.time()
        while self.times and now-self.times[0]>self.window: self.times.popleft()
        if len(self.times)<self.max: self.times.append(now); return True
        return False

class ConsistentHashRing:
    def __init__(self,replicas=3): self.replicas=replicas; self.ring={}; self.keys=[]
    def _hash(self,key): return int(__import__('hashlib').md5(key.encode()).hexdigest(),16)
    def add_node(self,node):
        for i in range(self.replicas):
            h=self._hash(f'{node}:{i}'); self.ring[h]=node; __import__('bisect').insort(self.keys,h)
    def remove_node(self,node):
        for i in range(self.replicas):
            h=self._hash(f'{node}:{i}')
            if h in self.ring: del self.ring[h]; self.keys.remove(h)
    def get_node(self,key):
        h=self._hash(key); idx=__import__('bisect').bisect_right(self.keys,h)%len(self.keys)
        return self.ring[self.keys[idx]]

class PubSub:
    def __init__(self): self._subs=defaultdict(list)
    def subscribe(self,topic,cb): self._subs[topic].append(cb)
    def unsubscribe(self,topic,cb):
        if cb in self._subs[topic]: self._subs[topic].remove(cb)
    def publish(self,topic,msg):
        for cb in self._subs[topic]: cb(msg)

class TaskQueue:
    def __init__(self): self.queue=deque()
    def enqueue(self,task_fn,*args): self.queue.append((task_fn,args))
    def process_one(self):
        if self.queue: fn,args=self.queue.popleft(); fn(*args)
    def process_all(self):
        while self.queue: self.process_one()
