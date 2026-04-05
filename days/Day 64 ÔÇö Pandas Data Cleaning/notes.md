# Day 64 — Pandas Data Cleaning

## Key syntax
```python
df.duplicated(); df.drop_duplicates(subset=['col'], keep='first')
df['col'].str.lower(); df['col'].str.strip(); df['col'].str.replace(r'[^a-z]','',regex=True)
df['date']=pd.to_datetime(df['date']); df['date'].dt.year; df['date'].dt.month
df['col'].apply(fn)                # apply row by row
df.apply(fn, axis=1)              # apply across columns

# Outlier removal
mean=df['col'].mean(); std=df['col'].std()
df[abs(df['col']-mean) <= 3*std]

# Merge
pd.merge(left,right,on='key',how='left')
```

## Interview tips
- Always check for duplicates and nulls first — `df.info()` and `df.isnull().sum()`
- Use `.str` accessor for vectorised string operations — much faster than `.apply()`
- `pd.to_datetime()` handles many formats automatically
