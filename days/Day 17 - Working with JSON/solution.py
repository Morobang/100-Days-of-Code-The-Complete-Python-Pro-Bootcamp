# Day 17 — JSON — SOLUTIONS
import json, os

def save_config(config, path):
    with open(path,'w') as f:
        json.dump(config, f, indent=2)

def load_config(path):
    try:
        with open(path) as f: return json.load(f)
    except FileNotFoundError: return {}

raw = '[{"name":"Rocket","score":9500},{"name":"Alice","score":7800},{"name":"Bob","score":8700}]'
players = json.loads(raw)
top = [p['name'] for p in sorted(players, key=lambda p: p['score'], reverse=True) if p['score'] > 8000]
print(top)

def merge_json(file1, file2, output):
    with open(file1) as f: d1 = json.load(f)
    with open(file2) as f: d2 = json.load(f)
    with open(output,'w') as f: json.dump({**d1, **d2}, f, indent=2)
