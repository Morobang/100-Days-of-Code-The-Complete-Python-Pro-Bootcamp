# Day 35: Project — Word Counter

**Phase:** 2 — Data Structures  
**Difficulty:** ⭐⭐⭐

## Project description

Build a word frequency analyser. The user types or pastes multi-line text (ending with a blank line), and the program produces a full analysis using every data structure skill from Phase 2.

## Requirements

1. **Collect input** — read lines until the user enters a blank line
2. **Count frequencies** — build a word frequency dict (case-insensitive, strip punctuation)
3. **Report:**
   - Total word count (including duplicates)
   - Number of unique words
   - Top 5 most frequent words with their counts
   - The 3 least frequent words
   - All words that appear exactly once
   - Unique first letters used (as a sorted list)
4. **Optional bonus:** ask the user for a word and report how many times it appears

## Example session

```
Enter text (blank line to finish):
> To be or not to be that is the question
> Whether tis nobler in the mind to suffer
>
Total words: 17
Unique words: 15
Top 5: the(2), to(3), be(2), ...
...
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Skeleton with TODO comments — start here |
| `solution/word_counter.py` | Complete solution |

## Concepts used
Days 1–34 — dict comprehensions, list comprehensions, set comprehensions, dicts, lists, sets, sorting, string methods
