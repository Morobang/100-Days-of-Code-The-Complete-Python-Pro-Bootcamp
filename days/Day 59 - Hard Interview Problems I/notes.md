# Day 59 — Hard Interview Problems I

## Problem patterns
| Problem | Key technique |
|---------|-------------|
| Median of stream | Two heaps (max-heap lower, min-heap upper) |
| Trapping rain water | Two pointers — process from sides inward |
| Largest rectangle | Monotonic stack |
| Word ladder | BFS on word graph |
| Alien dictionary | Topological sort |
| Max profit cooldown | DP with states (hold/sold/rest) |

## Hard problem mindset
- If O(n²) is obvious → look for O(n log n) or O(n) optimisation
- Two heaps → median, kth element problems
- Monotonic stack → "next greater/smaller element" family
- BFS → shortest path, word transformation
- Topological sort → ordering with dependencies

## Interview tips
- Talk through your approach before coding
- Start with the brute force, optimise step by step
- Verify time/space complexity before submitting
