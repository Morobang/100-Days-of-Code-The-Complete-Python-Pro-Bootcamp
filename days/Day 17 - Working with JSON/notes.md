# Day 17 — Working with JSON

## Key syntax
```python
import json

json.dumps(obj)                  # → JSON string
json.dumps(obj, indent=2)        # pretty
json.loads(json_string)          # → Python object

with open('f.json','w') as f:
    json.dump(obj, f, indent=2)  # write file

with open('f.json') as f:
    obj = json.load(f)           # read file
```

## Gotchas
- `dumps` (string) vs `dump` (file) — the 's' = string
- JSON keys must be strings — Python allows other types, JSON doesn't
- `True`/`False` → `true`/`false` in JSON (loaded back correctly)
- `None` → `null`

## Interview tips
- JSON everywhere in data engineering — APIs, configs, S3, Kafka
- Always wrap `json.loads()` in try/except for external data
- For large JSON, use `ijson` for streaming
