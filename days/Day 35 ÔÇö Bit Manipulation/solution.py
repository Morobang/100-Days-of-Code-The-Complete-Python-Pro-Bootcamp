# Day 35 — Bit Manipulation — SOLUTIONS

def is_odd(n): return bool(n & 1)

def is_power_of_two(n): return n > 0 and (n & (n-1)) == 0

def count_bits(n):
    count=0
    while n: count+=n&1; n>>=1
    return count

def single_number(lst):
    result=0
    for n in lst: result^=n
    return result

def missing_number(lst):
    n=len(lst)
    return n*(n+1)//2 - sum(lst)

def reverse_bits(n):
    result=0
    for _ in range(32): result=(result<<1)|(n&1); n>>=1
    return result

def two_single_numbers(lst):
    xor=0
    for n in lst: xor^=n
    bit=xor&(-xor)  # rightmost set bit
    a=b=0
    for n in lst:
        if n&bit: a^=n
        else: b^=n
    return (a,b)

def add_bits(a,b):
    mask=0xFFFFFFFF
    while b&mask:
        carry=(a&b)<<1; a^=b; b=carry
    return a if b==0 else a&mask
