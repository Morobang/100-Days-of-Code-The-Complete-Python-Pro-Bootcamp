# Day 35 — Bit Manipulation

## Key tricks
```python
n & 1            # is n odd?
n & (n-1)        # clear lowest set bit
n & (n-1) == 0   # is power of 2? (n>0)
n ^ n == 0       # XOR with itself = 0
a ^ b ^ a == b   # XOR cancels pairs
bin(n).count('1') # count set bits

# Check bit k
(n >> k) & 1

# Set bit k
n | (1 << k)

# Clear bit k
n & ~(1 << k)
```

## Gotchas
- Python integers are arbitrary precision — no 32-bit overflow
- `~n == -(n+1)` in Python (two's complement)
- `n & (n-1)` removes exactly the lowest set bit

## Interview tips
- Single number → XOR all elements (pairs cancel)
- Missing number → XOR 0..n with all elements
- Is power of 2 → `n>0 and (n&(n-1))==0`
