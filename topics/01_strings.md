# 📝 Strings

## Creating strings
```python
s = "hello"
s = 'hello'
s = """multiline
string"""
```

## Key methods
```python
s.upper()           # "HELLO"
s.lower()           # "hello"
s.strip()           # removes whitespace both ends
s.split(",")        # splits into list
",".join(["a","b"]) # joins list into string
s.replace("a","b")  # replace substring
s.find("ell")       # returns index, -1 if not found
s.startswith("he")  # True
s.endswith("lo")    # True
s.count("l")        # 2
s.isdigit()         # True if all digits
s.isalpha()         # True if all letters
```

## Slicing
```python
s = "hello"
s[0]     # "h"
s[-1]    # "o"
s[1:3]   # "el"
s[::-1]  # "olleh" reversed
```

## Formatting
```python
name = "Rocket"
f"Hello {name}"           # f-string (preferred)
f"{3.14:.2f}"             # "3.14"
f"{1000000:,}"            # "1,000,000"
```

## Gotchas
- Strings are **immutable**
- Use `in` for membership: `"ell" in "hello"` True
