# Day 26 — Generators — SOLUTIONS

def my_range(start,stop,step=1):
    cur=start
    while cur<stop: yield cur; cur+=step

def fib_gen():
    a,b=0,1
    while True: yield a; a,b=b,a+b

def chunked(iterable,size):
    chunk=[]
    for item in iterable:
        chunk.append(item)
        if len(chunk)==size: yield chunk; chunk=[]
    if chunk: yield chunk

def running_avg():
    total=count=0
    while True:
        val=(yield total/count if count else None)
        if val is not None: total+=val; count+=1

def take_while(pred,iterable):
    for item in iterable:
        if not pred(item): break
        yield item

def flatten(nested):
    for item in nested:
        if isinstance(item,(list,tuple)): yield from flatten(item)
        else: yield item

def read_numbers(lst):
    for n in lst: yield n

def square(gen):
    for n in gen: yield n**2

def only_even(gen):
    for n in gen:
        if n%2==0: yield n
