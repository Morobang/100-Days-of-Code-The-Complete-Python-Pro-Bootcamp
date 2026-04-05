# Day 67 — APIs with requests

## Key syntax
```python
import requests

r = requests.get(url, params={'key':'val'}, timeout=10)
r = requests.post(url, json={'key':'val'}, headers={'Auth':'token'})
r.status_code   # 200, 404, 500
r.json()        # parse JSON response
r.text          # raw text
r.raise_for_status()  # raises HTTPError if 4xx/5xx

# Session (reuse connection)
with requests.Session() as s:
    s.headers['Authorization'] = 'Bearer token'
    r = s.get(url)

# Timeout
requests.get(url, timeout=(3.05, 27))  # (connect, read) timeout
```

## Error handling
```python
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()
except requests.exceptions.Timeout:
    print('Request timed out')
except requests.exceptions.HTTPError as e:
    print(f'HTTP error: {e}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
```

## Interview tips
- Always set a timeout — never let requests hang forever
- Use `Session` for multiple requests to the same server
- Exponential backoff: `time.sleep(backoff ** attempt)`
