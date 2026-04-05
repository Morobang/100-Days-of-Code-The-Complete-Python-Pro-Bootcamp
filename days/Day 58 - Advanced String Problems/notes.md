# Day 58 — Advanced String Problems

## Key patterns
```python
# Expand around centre (palindrome)
def expand(s, l, r):
    while l>=0 and r<len(s) and s[l]==s[r]: l-=1; r+=1
    return s[l+1:r]

# Edit distance DP
dp[i][j] = min(dp[i-1][j]+1,   # delete
               dp[i][j-1]+1,   # insert
               dp[i-1][j-1] + (0 if s1[i-1]==s2[j-1] else 1))  # replace

# Wildcard DP
if p[j-1]=='*': dp[i][j] = dp[i-1][j] or dp[i][j-1]
elif p[j-1]=='?' or s[i-1]==p[j-1]: dp[i][j] = dp[i-1][j-1]
```

## Complexity targets
| Problem | Time | Space |
|---------|------|-------|
| Longest palindromic substring | O(n²) | O(1) |
| Edit distance | O(mn) | O(mn) |
| LPS | O(n²) | O(n²) |
| Count subsequences | O(mn) | O(mn) |

## Interview tips
- Palindrome problems → expand around centre or DP
- "Minimum operations" → edit distance DP (classic)
- LCS (longest common subsequence) → foundation for many string DP problems
