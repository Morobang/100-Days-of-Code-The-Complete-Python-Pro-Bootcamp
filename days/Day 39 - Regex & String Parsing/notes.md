# Day 39 — Regex & String Parsing

## Key syntax
```python
import re

re.search(r'pattern', text)        # first match anywhere
re.match(r'pattern', text)         # match at START only
re.fullmatch(r'pattern', text)     # match ENTIRE string
re.findall(r'pattern', text)       # list of all matches
re.sub(r'pattern', replacement, text)  # replace
re.split(r'pattern', text)         # split on pattern

# Groups
m = re.search(r'(\d{4})-(\d{2})', '2025-03')
m.group()    # '2025-03'
m.groups()   # ('2025', '03')
m.group(1)   # '2025'

# Flags
re.IGNORECASE   # case insensitive
re.MULTILINE    # ^ and $ match per line
```

## Common patterns
```
\d    digit          \D  non-digit
\w    word char      \W  non-word
\s    whitespace     \S  non-whitespace
.     any (except \n)
^     start    $  end
*     0+   +  1+   ?  0 or 1
{n,m} n to m times
[abc] any of   [^abc] none of
```

## Interview tips
- Always use raw strings `r'...'`
- `.` matches anything — use `\.` for a literal dot
- `re.fullmatch` for validation, `re.search` for extraction
