# Day 75 — Performance — SOLUTIONS
import timeit, sys
from collections import Counter
from itertools import chain
from functools import lru_cache

def benchmark_lookup(n):
    lst=list(range(n)); s=set(range(n)); d=dict.fromkeys(range(n))
    target=n-1; reps=10000
    return {
        'list': timeit.timeit(lambda: target in lst, number=reps),
        'set':  timeit.timeit(lambda: target in s,   number=reps),
        'dict': timeit.timeit(lambda: target in d,   number=reps),
    }

def slow_word_count(text):
    words=text.split(); result={}
    for word in words: result[word]=words.count(word)
    return result

def fast_word_count(text): return dict(Counter(text.split()))

def flatten_loop(matrix):
    result=[]
    for row in matrix:
        for x in row: result.append(x)
    return result

def flatten_comp(matrix): return [x for row in matrix for x in row]
def flatten_chain(matrix): return list(chain.from_iterable(matrix))

class Point:
    def __init__(self,x,y): self.x=x; self.y=y

class FastPoint:
    __slots__=['x','y']
    def __init__(self,x,y): self.x=x; self.y=y

def compare_memory():
    return {'Point':sys.getsizeof(Point(1,2)),'FastPoint':sys.getsizeof(FastPoint(1,2))}

def compare_fib(n):
    def naive(k): return k if k<=1 else naive(k-1)+naive(k-2)
    @lru_cache(maxsize=None)
    def memo(k): return k if k<=1 else memo(k-1)+memo(k-2)
    def dp(k):
        a,b=0,1
        for _ in range(k): a,b=b,a+b
        return a
    small=min(n,25)  # naive is too slow for large n
    return {
        'naive': timeit.timeit(lambda:naive(small), number=10),
        'memo':  timeit.timeit(lambda:memo(n), number=1000),
        'dp':    timeit.timeit(lambda:dp(n), number=1000),
    }

def memory_comparison(n):
    return {'list':sys.getsizeof(list(range(n))),'generator':sys.getsizeof(x for x in range(n))}
