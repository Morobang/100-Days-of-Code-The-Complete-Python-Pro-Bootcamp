# Day 28 — OOP Deep Dive — SOLUTIONS
import time
from collections import OrderedDict

class Stack:
    def __init__(self): self._data=[]
    def push(self,item): self._data.append(item)
    def pop(self):
        if self.is_empty(): raise IndexError('pop from empty stack')
        return self._data.pop()
    def peek(self):
        if self.is_empty(): raise IndexError('peek from empty stack')
        return self._data[-1]
    def is_empty(self): return not self._data
    def size(self): return len(self._data)
    def __str__(self): return f'Stack({self._data})'

class Queue:
    def __init__(self): self._data=[]
    def enqueue(self,item): self._data.append(item)
    def dequeue(self):
        if self.is_empty(): raise IndexError('dequeue from empty queue')
        return self._data.pop(0)
    def front(self): return self._data[0] if self._data else None
    def is_empty(self): return not self._data
    def size(self): return len(self._data)

class LRUCache:
    def __init__(self,capacity): self.cap=capacity; self.cache=OrderedDict()
    def get(self,key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key); return self.cache[key]
    def put(self,key,val):
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key]=val
        if len(self.cache)>self.cap: self.cache.popitem(last=False)

class MinStack:
    def __init__(self): self._data=[]; self._mins=[]
    def push(self,val):
        self._data.append(val)
        self._mins.append(min(val, self._mins[-1] if self._mins else val))
    def pop(self): self._data.pop(); self._mins.pop()
    def get_min(self): return self._mins[-1]

class NumberRange:
    def __init__(self,start,end): self.current=start; self.end=end
    def __iter__(self): return self
    def __next__(self):
        if self.current>self.end: raise StopIteration
        val=self.current; self.current+=1; return val

class Timer:
    def __enter__(self): self.start=time.time(); return self
    def __exit__(self,*args): self.elapsed=time.time()-self.start; return False
