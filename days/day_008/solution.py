# Day 008 — Loops — REFERENCE SOLUTION

def primes_up_to(n: int) -> list:
    # Sieve of Eratosthenes: start with all True, mark composites False
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def pascals_triangle(rows: int) -> list:
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)          # start with all 1s
        for j in range(1, i):        # fill in middle values
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


def digit_sum(n: int) -> int:
    # Convert to string, iterate digits, convert back to int, sum
    return sum(int(d) for d in str(abs(n)))


def is_power_of_two(n: int) -> bool:
    # Bit trick: powers of 2 have exactly one 1-bit
    # n & (n-1) clears the lowest set bit — result is 0 for powers of 2
    return n > 0 and (n & (n - 1)) == 0
