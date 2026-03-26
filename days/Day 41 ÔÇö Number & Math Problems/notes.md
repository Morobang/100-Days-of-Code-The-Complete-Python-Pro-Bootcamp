# Day 41 — Number & Math Problems

## Key tools
```python
from math import gcd, sqrt, factorial, log2
from itertools import count

# Euclidean GCD
def gcd(a,b): return a if b==0 else gcd(b, a%b)

# Is prime O(√n)
def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return False
    return True

# Sieve of Eratosthenes
def sieve(n):
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i,p in enumerate(s) if p]
```

## Gotchas
- Integer palindrome: negative numbers are never palindromes
- Power of 3: `3**19 = 1162261467` is the largest int32 power of 3
- Happy number: use a seen set to detect cycles

## Interview tips
- GCD → Euclidean algorithm (interview classic)
- Is prime → O(√n) trial division
- "Without built-ins" → know how to implement from scratch
