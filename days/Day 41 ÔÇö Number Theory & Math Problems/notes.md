# Day 41 — Number Theory & Math Problems

## Key tools
```python
from math import gcd, sqrt, floor, ceil, log2
from functools import reduce

lcm = lambda a,b: abs(a*b)//gcd(a,b)
lcm_list = lambda lst: reduce(lcm, lst)

# Sieve of Eratosthenes
def sieve(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i,v in enumerate(s) if v]
```

## Gotchas
- `gcd(0, n) == n` — be careful with 0
- For `is_prime`, only check up to `sqrt(n)` — O(sqrt(n))
- Roman numerals: process largest values first, handle subtractive pairs

## Interview tips
- "Count primes" → Sieve of Eratosthenes
- Happy number → Floyd's cycle detection or seen set
- GCD/LCM come up in fraction simplification
