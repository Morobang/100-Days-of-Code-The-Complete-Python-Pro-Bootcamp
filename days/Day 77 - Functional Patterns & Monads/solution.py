# Day 77 — Functional Patterns — SOLUTIONS
import math

class Maybe:
    def __init__(self,v): self._v=v
    def map(self,fn): return Maybe(fn(self._v)) if self._v is not None else self
    def bind(self,fn): return fn(self._v) if self._v is not None else self
    def filter(self,pred): return self if self._v is not None and pred(self._v) else Maybe(None)
    def get_or(self,default): return self._v if self._v is not None else default

class Ok:
    def __init__(self,v): self.value=v
    def bind(self,fn): return fn(self.value)
    def map(self,fn): return Ok(fn(self.value))
    def get_or(self,default): return self.value

class Err:
    def __init__(self,e): self.error=e
    def bind(self,fn): return self
    def map(self,fn): return self
    def get_or(self,default): return default

def safe_parse_int(s):
    try: return Ok(int(s))
    except ValueError: return Err(f'Not an int: {s}')

def safe_divide(a,b):
    return Err('Division by zero') if b==0 else Ok(a/b)

def safe_sqrt(n):
    return Err('Negative sqrt') if n<0 else Ok(math.sqrt(n))

def trampoline(fn):
    def wrapper(*args,**kwargs):
        result=fn(*args,**kwargs)
        while callable(result): result=result()
        return result
    return wrapper

def fmap(fn,container):
    if isinstance(container,list): return [fn(x) for x in container]
    if isinstance(container,(Maybe,Ok,Err)): return container.map(fn)
    return fn(container)
