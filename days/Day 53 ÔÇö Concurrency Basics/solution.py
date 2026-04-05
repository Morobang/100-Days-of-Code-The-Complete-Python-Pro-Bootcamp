# Day 53 — Concurrency — SOLUTIONS
import threading, queue, time, asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

class SafeCounter:
    def __init__(self): self.value=0; self._lock=threading.Lock()
    def increment(self):
        with self._lock: self.value+=1
    def get(self): return self.value

def parallel_squares(nums):
    with ThreadPoolExecutor() as ex:
        return list(ex.map(lambda n:n*n, nums))

def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

def find_primes_parallel(lst):
    with ProcessPoolExecutor() as ex:
        return [n for n,p in zip(lst,ex.map(is_prime,lst)) if p]

async def fetch(url):
    await asyncio.sleep(0.01)
    return f'data from {url}'

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

async def rate_limited_fetch(urls,max_concurrent):
    sem=asyncio.Semaphore(max_concurrent)
    async def limited(url):
        async with sem: return await fetch(url)
    return await asyncio.gather(*[limited(u) for u in urls])

def producer(q,items):
    for item in items: q.put(item)
    q.put(None)  # sentinel

def consumer(q,results):
    while True:
        item=q.get()
        if item is None: break
        results.append(item*2)
