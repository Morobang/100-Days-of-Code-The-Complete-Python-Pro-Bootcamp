# Day 77 — Functional Patterns

## Monad laws
1. **Left identity**: `Ok(a).bind(f) == f(a)`
2. **Right identity**: `Ok(a).bind(Ok) == Ok(a)`
3. **Associativity**: `m.bind(f).bind(g) == m.bind(lambda x: f(x).bind(g))`

## When to use
- `Maybe` → nullable values, optional lookups
- `Result` → error handling without try/except chains
- `List` → non-deterministic computations

## Python idioms that are monadic
- `Optional` chaining with `.get()`
- Generator comprehensions
- `itertools.chain`
