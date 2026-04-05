# Day 68 — Environment Variables & Config

## Key syntax
```python
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv('.env')              # loads .env into os.environ

os.environ['KEY']                # KeyError if missing
os.environ.get('KEY', 'default')  # safe
os.getenv('KEY', 'default')     # same

# .env file format
# DB_HOST=localhost
# DB_PORT=5432
# DEBUG=true
# API_KEY=secret123
```

## Config patterns
```python
# Typed config from env
import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', '5432'))
    DEBUG   = os.getenv('DEBUG', 'false').lower() == 'true'
```

## Gotchas
- Environment variables are always strings — cast to int/bool/float as needed
- Never commit .env files — add to .gitignore
- Use `os.getenv` not `os.environ[]` to avoid KeyError

## Interview tips
- Secrets (API keys, passwords) should NEVER be in source code
- Use env vars for config that changes between environments (dev/staging/prod)
- `python-dotenv` is the standard library for .env files
