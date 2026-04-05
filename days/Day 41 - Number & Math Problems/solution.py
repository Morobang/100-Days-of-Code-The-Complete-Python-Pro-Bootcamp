# Day 41 — Number & Math — SOLUTIONS

def fizzbuzz(n):
    return ['FizzBuzz' if i%15==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else str(i) for i in range(1,n+1)]

def count_digits(n):
    return {d:str(n).count(d) for d in set(str(n))}

def is_palindrome_num(n):
    if n<0 or (n%10==0 and n!=0): return False
    rev=0; orig=n
    while n>0: rev=rev*10+n%10; n//=10
    return orig==rev

def prime_factors(n):
    factors=[]; d=2
    while d*d<=n:
        while n%d==0: factors.append(d); n//=d
        d+=1
    if n>1: factors.append(n)
    return factors

def my_gcd(a,b): return a if b==0 else my_gcd(b,a%b)
def my_lcm(a,b): return a*b//my_gcd(a,b)

def is_power_of_three(n):
    return n>0 and 1162261467%n==0

def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    for i in range(len(s)):
        if i+1<len(s) and vals[s[i]]<vals[s[i+1]]: total-=vals[s[i]]
        else: total+=vals[s[i]]
    return total

def int_to_roman(n):
    vals=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
          (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result=''
    for v,r in vals:
        while n>=v: result+=r; n-=v
    return result

def int_sqrt(n):
    if n<2: return n
    lo,hi=1,n//2
    while lo<=hi:
        mid=(lo+hi)//2
        if mid*mid==n: return mid
        elif mid*mid<n: lo=mid+1
        else: hi=mid-1
    return hi

def is_happy(n):
    seen=set()
    while n!=1:
        if n in seen: return False
        seen.add(n); n=sum(int(d)**2 for d in str(n))
    return True

def count_primes(n):
    if n<2: return 0
    sieve=[True]*n; sieve[0]=sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n,i): sieve[j]=False
    return sum(sieve)
