# Day 39 — Regex — SOLUTIONS
import re

def is_valid_email(s):
    return bool(re.fullmatch(r'[\w.+-]+@[\w-]+\.[\w.]+',s))

def extract_numbers(text):
    return [float(n) if '.' in n else int(n) for n in re.findall(r'\d+\.?\d*',text)]

def is_valid_phone(s):
    return bool(re.fullmatch(r'(\+27|0)\d{9}|\d{3}-\d{3}-\d{4}',s))

def extract_urls(text):
    return re.findall(r'https?://\S+',text)

def censor(text,words):
    for w in words: text=re.sub(re.escape(w),'****',text,flags=re.IGNORECASE)
    return text

def parse_config(text):
    return dict(re.findall(r'(\w+)=(\S+)',text))

def tokenise(expr):
    return re.findall(r'\d+\.?\d*|[a-zA-Z_]\w*|[+\-*/^()=]',expr)

def md_bold(text):
    return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',text)
