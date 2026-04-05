# Day 41 — Number Theory — SOLUTIONS
from math import gcd
from functools import reduce
import heapq

def gcd_list(lst): return reduce(gcd, lst)
def lcm_list(lst): return reduce(lambda a,b: abs(a*b)//gcd(a,b), lst)

def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

def count_primes(n):
    if n<2: return 0
    s=[True]*n; s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n,i): s[j]=False
    return sum(s)

def prime_factors(n):
    factors=[]; d=2
    while d*d<=n:
        while n%d==0: factors.append(d); n//=d
        d+=1
    if n>1: factors.append(n)
    return factors

def is_happy(n):
    seen=set()
    while n!=1:
        if n in seen: return False
        seen.add(n); n=sum(int(d)**2 for d in str(n))
    return True

def col_title(n):
    result=''
    while n:
        n-=1; result=chr(n%26+65)+result; n//=26
    return result

def is_ugly(n):
    if n<=0: return False
    for f in [2,3,5]:
        while n%f==0: n//=f
    return n==1

def nth_ugly(n):
    ugly=[1]; i2=i3=i5=0
    for _ in range(n-1):
        nxt=min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
        ugly.append(nxt)
        if nxt==ugly[i2]*2: i2+=1
        if nxt==ugly[i3]*3: i3+=1
        if nxt==ugly[i5]*5: i5+=1
    return ugly[-1]

def to_roman(n):
    vals=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
          (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result=''
    for v,s in vals:
        while n>=v: result+=s; n-=v
    return result

def from_roman(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result=0
    for i in range(len(s)):
        if i+1<len(s) and vals[s[i]]<vals[s[i+1]]: result-=vals[s[i]]
        else: result+=vals[s[i]]
    return result
