# Day 27 — Decorators — SOLUTIONS
from functools import wraps
import time

def make_counter(start=0):
    count=[start]
    def counter(): count[0]+=1; return count[0]
    return counter

def make_multiplier(factor):
    return lambda x: x*factor

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print(f'{func.__name__} took {time.time()-start:.4f}s')
        return result
    return wrapper

def memoize(func):
    cache={}
    @wraps(func)
    def wrapper(*args):
        if args not in cache: cache[args]=func(*args)
        return cache[args]
    return wrapper

def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(times):
                try: return func(*args,**kwargs)
                except Exception:
                    if attempt==times-1: raise
        return wrapper
    return decorator

def validate_args(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i,(arg,t) in enumerate(zip(args,types)):
                if not isinstance(arg,t):
                    raise TypeError(f'Arg {i}: expected {t.__name__}, got {type(arg).__name__}')
            return func(*args,**kwargs)
        return wrapper
    return decorator

def rate_limit(calls,period):
    def decorator(func):
        history=[]
        @wraps(func)
        def wrapper(*args,**kwargs):
            now=time.time()
            history[:]=[ t for t in history if now-t<period]
            if len(history)>=calls: raise RuntimeError('Rate limit exceeded')
            history.append(now)
            return func(*args,**kwargs)
        return wrapper
    return decorator
