# Day 18 — Modules & Imports

## Key syntax
```python
import math
import random
import os
import string
from datetime import datetime, date, timedelta
from pathlib import Path

# math
math.pi, math.e
math.sqrt(x), math.ceil(x), math.floor(x)
math.log(x), math.log10(x)
math.factorial(n)

# random
random.randint(a, b)       # int a <= x <= b
random.random()            # float 0.0–1.0
random.choice(seq)         # pick one item
random.shuffle(lst)        # shuffle in place
random.sample(seq, k)      # k unique items

# string constants
string.ascii_letters       # 'abcABC...'
string.digits              # '0123456789'
string.punctuation         # '!"#$%...'

# datetime
datetime.now()
date.today()
d.strftime('%Y-%m-%d')     # format
datetime.strptime(s, fmt)  # parse string to datetime
timedelta(days=7)          # date arithmetic
```

## Gotchas
- `import random` then `random.randint` vs `from random import randint`
- `random.shuffle()` modifies in place, returns None
- `os.path.join()` is platform-safe — never concatenate paths with `+`

## Interview tips
- Know the standard library — shows you don't reinvent the wheel
- `pathlib.Path` is the modern way to handle file paths (over `os.path`)
- `datetime` is essential for data engineering — timestamps everywhere
