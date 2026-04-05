# Day 56 — Context Managers & Protocols — SOLUTIONS
import time, tempfile, os
from contextlib import contextmanager

class Timer:
    def __enter__(self): self.start=time.time(); return self
    def __exit__(self,*args): self.elapsed=time.time()-self.start

@contextmanager
def temp_file(content):
    f=tempfile.NamedTemporaryFile(mode='w',delete=False,suffix='.txt')
    f.write(content); f.close()
    try: yield f.name
    finally: os.unlink(f.name)

@contextmanager
def retry(times=3):
    last=None
    for attempt in range(times):
        try: yield; return
        except Exception as e: last=e
    raise last

class FibSequence:
    def __init__(self,n):
        self._nums=[0,1]
        while len(self._nums)<n:
            self._nums.append(self._nums[-1]+self._nums[-2])
        self._nums=self._nums[:n]
    def __len__(self): return len(self._nums)
    def __getitem__(self,i): return self._nums[i]
    def __contains__(self,x): return x in self._nums
    def __iter__(self): return iter(self._nums)

class CaseInsensitiveDict:
    def __init__(self): self._data={}
    def __setitem__(self,key,val): self._data[key.lower()]=val
    def __getitem__(self,key): return self._data[key.lower()]
    def __contains__(self,key): return key.lower() in self._data
    def __repr__(self): return repr(self._data)
