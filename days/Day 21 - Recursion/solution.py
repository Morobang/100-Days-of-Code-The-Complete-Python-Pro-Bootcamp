# Day 21 — Recursion — SOLUTIONS

def rsum(lst): return 0 if not lst else lst[0]+rsum(lst[1:])
def power(base, exp): return 1 if exp==0 else base*power(base,exp-1)
def reverse(s): return s if len(s)<=1 else reverse(s[1:])+s[0]
def count(lst, target): return 0 if not lst else (1 if lst[0]==target else 0)+count(lst[1:],target)

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n): return n if n<=1 else fib(n-1)+fib(n-2)

def flatten(lst):
    result=[]
    for item in lst:
        if isinstance(item,list): result.extend(flatten(item))
        else: result.append(item)
    return result

def binary_search(lst, target, lo=0, hi=None):
    if hi is None: hi=len(lst)-1
    if lo>hi: return -1
    mid=(lo+hi)//2
    if lst[mid]==target: return mid
    elif lst[mid]<target: return binary_search(lst,target,mid+1,hi)
    else: return binary_search(lst,target,lo,mid-1)

def hanoi(n, source, target, auxiliary):
    if n==1:
        print(f'Move disk 1 from {source} to {target}'); return
    hanoi(n-1,source,auxiliary,target)
    print(f'Move disk {n} from {source} to {target}')
    hanoi(n-1,auxiliary,target,source)
