# Day 67 — APIs — SOLUTIONS
import requests, time

def get_json(url):
    try:
        r=requests.get(url,timeout=10); r.raise_for_status(); return r.json()
    except Exception: return None

def post_json(url,data,headers=None):
    try:
        r=requests.post(url,json=data,headers=headers or {},timeout=10)
        r.raise_for_status(); return r.json()
    except Exception as e: return {'error':str(e)}

class APIClient:
    def __init__(self,base_url,api_key):
        self.base=base_url.rstrip('/')
        self.session=requests.Session()
        self.session.headers['Authorization']=f'Bearer {api_key}'
    def get(self,endpoint,params=None):
        r=self.session.get(f'{self.base}/{endpoint}',params=params,timeout=10)
        r.raise_for_status(); return r.json()
    def post(self,endpoint,data):
        r=self.session.post(f'{self.base}/{endpoint}',json=data,timeout=10)
        r.raise_for_status(); return r.json()

def rate_limited_get(urls,delay=0.5):
    results=[]
    for url in urls:
        results.append(get_json(url))
        time.sleep(delay)
    return results

def get_with_retry(url,retries=3,backoff=2):
    for attempt in range(retries):
        try:
            r=requests.get(url,timeout=10); r.raise_for_status(); return r.json()
        except Exception:
            if attempt==retries-1: raise
            time.sleep(backoff**attempt)
