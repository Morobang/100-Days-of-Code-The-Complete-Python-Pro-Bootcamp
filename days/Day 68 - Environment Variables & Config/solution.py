# Day 68 — Config — SOLUTIONS
import os

def get_env(key,default=None): return os.environ.get(key,default)

from dataclasses import dataclass
@dataclass
class Config:
    db_host:str='localhost'; db_port:int=5432; debug:bool=False; api_key:str=''
    @classmethod
    def from_env(cls):
        return cls(
            db_host=os.getenv('DB_HOST','localhost'),
            db_port=int(os.getenv('DB_PORT','5432')),
            debug=os.getenv('DEBUG','false').lower()=='true',
            api_key=os.getenv('API_KEY','')
        )

def load_dotenv(filepath='.env'):
    try:
        with open(filepath) as f:
            for line in f:
                line=line.strip()
                if not line or line.startswith('#'): continue
                if '=' in line:
                    key,_,val=line.partition('=')
                    os.environ.setdefault(key.strip(),val.strip())
    except FileNotFoundError: pass

def validate_config(required_keys):
    missing=[k for k in required_keys if not os.environ.get(k)]
    if missing: raise ValueError(f'Missing required env vars: {missing}')

def load_config(defaults,env_prefix='APP'):
    result=dict(defaults)
    for key in defaults:
        env_key=f'{env_prefix}_{key.upper()}'
        if env_key in os.environ: result[key]=os.environ[env_key]
    return result
