# Day 009 — Functions: Basics & Scope — REFERENCE SOLUTION

def make_counter(start: int = 0):
    # 'count' lives in the enclosing scope of inner()
    # nonlocal lets inner() modify it (otherwise it would create a local)
    count = start
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


def apply_twice(fn, x):
    # Functions are first-class — fn is just a variable holding a function
    return fn(fn(x))


x = 'global'

def demonstrate_scope():
    x = 'enclosing'
    def inner():
        x = 'local'
        return x
    inner_val = inner()
    # This function's x is 'enclosing', globals()['x'] is 'global'
    return (globals()['x'], x, inner_val)
