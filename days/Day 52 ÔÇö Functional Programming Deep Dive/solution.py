# Day 52 — Functional Programming — SOLUTIONS
from functools import reduce
from itertools import islice
import time, inspect

def pipeline(*fns): return lambda x: reduce(lambda v,f: f(v), fns, x)
def compose(*fns):  return lambda x: reduce(lambda v,f: f(v), reversed(fns), x)

def curry(fn):
    n=len(inspect.signature(fn).parameters)
    def curried(*args):
        if len(args)>=n: return fn(*args)
        return lambda *a: curried(*(args+a))
    return curried

def memoize_ttl(seconds):
    def decorator(fn):
        cache={}
        @__import__('functools').wraps(fn)
        def wrapper(*args):
            now=time.time()
            if args in cache and now-cache[args][1]<seconds:
                return cache[args][0]
            result=fn(*args); cache[args]=(result,now)
            return result
        return wrapper
    return decorator

def deep_flatten(iterable):
    for item in iterable:
        try:
            if isinstance(item,str): yield item; continue
            yield from deep_flatten(item)
        except TypeError: yield item

def group_and_agg(records,key_fn,agg_fn):
    groups={}
    for r in records: groups.setdefault(key_fn(r),[]).append(r)
    return {k:agg_fn(v) for k,v in groups.items()}

def zip_longest(*iterables,default=None):
    iters=[iter(it) for it in iterables]
    sentinel=object()
    while True:
        vals=[next(it,sentinel) for it in iters]
        if all(v is sentinel for v in vals): return
        yield tuple(default if v is sentinel else v for v in vals)

def chunk_iter(iterable,n):
    it=iter(iterable)
    while True:
        chunk=tuple(islice(it,n))
        if not chunk: return
        yield chunk
