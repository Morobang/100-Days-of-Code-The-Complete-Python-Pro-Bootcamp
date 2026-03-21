# 🗂️ Dictionaries & Sets

## Dictionaries
```python
d = {"name": "Rocket", "age": 23}

d["name"]               # access — KeyError if missing
d.get("name")           # None if missing
d.get("x", "default")  # custom default

d["city"] = "Pretoria"  # add/update
del d["age"]            # delete key
d.pop("age", None)      # pop with default

d.keys()
d.values()
d.items()               # (key, value) pairs

d.update({"x": 1})      # merge
{**d, "extra": 99}      # spread merge
"name" in d             # True
```

## Sets
```python
s = {1, 2, 3}
s.add(4)
s.discard(3)    # no error if missing

a = {1, 2, 3}
b = {2, 3, 4}
a | b    # union         {1,2,3,4}
a & b    # intersection  {2,3}
a - b    # difference    {1}

# Deduplicate a list
unique = list(set([1,1,2,2,3]))
```

## Gotchas
- Dict keys must be hashable (not lists)
- Sets are unordered — no indexing
