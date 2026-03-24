# Day 20 — Modules, pip & Virtual Environments

## Key syntax
```python
import math
from datetime import datetime, date, timedelta
import random, os, string

math.pi  math.sqrt(x)  math.ceil(x)  math.floor(x)

random.randint(a, b)      # a <= x <= b
random.random()           # 0.0–1.0
random.choice(seq)
random.shuffle(lst)       # in place
random.sample(seq, k)     # k unique items

date.today()
datetime.now()
d.strftime('%Y-%m-%d')
timedelta(days=7)

string.ascii_letters   string.digits   string.punctuation
```

## Virtual environments
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
pip install requests
pip freeze > requirements.txt
deactivate
```

## Gotchas
- `random.shuffle()` modifies in place, returns None
- `os.path.join()` not string `+` for file paths
- Commit `requirements.txt`, never commit `venv/`

## Interview tips
- Standard library knowledge shows you don't reinvent the wheel
- `pathlib.Path` is the modern `os.path` replacement
- `datetime` is essential for data engineering — timestamps everywhere
