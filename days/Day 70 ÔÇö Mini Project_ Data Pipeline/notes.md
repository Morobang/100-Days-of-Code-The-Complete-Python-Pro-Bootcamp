# Day 70 — Mini Project: Data Pipeline

## ETL Pipeline Pattern
```
Extract  → Fetch from API/file/DB
Transform → Clean, validate, reshape
Load     → Write to DB/file/warehouse
```

## Pipeline checklist
- [ ] Extract with error handling + retries
- [ ] Validate schema before transform
- [ ] Transform is pure (no side effects)
- [ ] Load is idempotent (safe to re-run)
- [ ] Log each stage
- [ ] Return summary metrics

## What this combines
- `requests` → Extract
- `pandas` → Transform
- `sqlite3` → Load
- `csv` → Export
- `logging` → Observability

## Interview tips
- Real data pipelines are rarely one-shot — design for re-runs
- Idempotency: running twice gives same result as running once
- Separate concerns: extract, transform, load are different functions
