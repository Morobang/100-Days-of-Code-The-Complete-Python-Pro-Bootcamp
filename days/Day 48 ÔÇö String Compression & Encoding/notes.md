# Day 48 — String Compression & Encoding

## Key patterns
```python
# Run-length encode
i=0; result=[]
while i<len(s):
    char=s[i]; count=1
    while i+count<len(s) and s[i+count]==char: count+=1
    result.append(f'{count}{char}'); i+=count

# Safe encode (length-prefix protocol)
def encode(strs):
    return ''.join(f'{len(s)}#{s}' for s in strs)

def decode(s):
    result=[]; i=0
    while i<len(s):
        j=s.index('#',i)
        n=int(s[i:j]); i=j+1
        result.append(s[i:i+n]); i+=n
    return result
```

## Gotchas
- `#` delimiter fails if strings contain `#` — use length-prefix instead
- Base 16 digits: `'0123456789abcdef'`
- Decode ways: check both single and double digit mappings

## Interview tips
- Serialise tree: preorder with null markers (`#`)
- Decode ways: DP — `dp[i] = dp[i-1] + dp[i-2]` (if valid 2-digit)
- Length-prefix encoding is robust against any character in input
