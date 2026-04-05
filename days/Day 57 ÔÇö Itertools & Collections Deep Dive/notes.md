# Day 57 — Itertools & Collections

## itertools cheat sheet
```python
count(start, step)           # infinite counter
cycle(iterable)              # infinite cycle
repeat(val, n)               # repeat n times
chain(a, b, c)               # merge iterables
islice(it, stop)             # lazy slice
takewhile(pred, it)          # take while True
dropwhile(pred, it)          # skip while True
groupby(it, key=fn)          # group consecutive
accumulate(it, fn=add)       # running totals
combinations(it, r)          # C(n,r) — no repeats
permutations(it, r)          # P(n,r)
product(a, b)                # cartesian product
starmap(fn, pairs)           # fn(*pair) for each pair
```

## collections cheat sheet
```python
Counter(iterable)            # frequency map
Counter.most_common(n)       # top n
defaultdict(list)            # auto-default
deque(maxlen=n)              # fixed-size ring buffer
namedtuple('T', ['x','y'])   # lightweight class
OrderedDict()                # ordered + move_to_end
```

## Interview tips
- `Counter` → frequency problems
- `deque(maxlen=n)` → sliding window, recent items
- `namedtuple` → data records with named fields (lighter than dataclass)
- `defaultdict(list)` → graph adjacency lists
