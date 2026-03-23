# Day 002 — String Methods

## Key syntax
```python
s.split()          # split on whitespace
s.split(",")       # split on delimiter
",".join(lst)      # join list into string
s.strip(".,!?")    # strip specific chars from both ends
s.replace("a","b") # replace all occurrences
s.count("l")       # count occurrences of substring
ord("a")           # → 97 (ASCII code)
chr(97)            # → "a" (char from ASCII code)
```

## Gotchas
- `.split()` with no args splits on any whitespace AND removes empty strings
- `.strip()` strips characters, not substrings — `"ab".strip("ba")` → `""`
- `ord()` / `chr()` is essential for cipher problems — uppercase A=65, lowercase a=97

## Interview tips
- Run-length encoding is a classic compression interview question — know it cold
- Word frequency is asked as "find most common element" — build freq dict, then `max(d, key=d.get)`
- Caesar cipher follow-up: "make it work with any Unicode" — mention `ord`/`chr` approach
