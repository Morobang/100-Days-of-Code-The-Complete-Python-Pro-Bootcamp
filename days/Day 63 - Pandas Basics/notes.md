# Day 63 — Pandas Basics

## Key syntax
```python
import pandas as pd

df = pd.read_csv('file.csv')
df.head(5); df.tail(5); df.info(); df.describe()
df.shape; df.columns; df.dtypes; df.isnull().sum()

# Select
df['col']; df[['a','b']]; df.iloc[0]; df.loc[0,'col']

# Filter
df[df['col'] > 5]
df[(df['a']>1) & (df['b']<10)]
df.query('a > 1 and b < 10')

# Sort
df.sort_values('col', ascending=False)

# Add column
df['new'] = df['a'] + df['b']

# Missing values
df.dropna(); df.fillna(0); df.fillna(df.median())

# Group
df.groupby('col').agg({'price':'mean','count':'size'})

# Pivot
df.pivot_table(index='date',columns='product',values='amount',aggfunc='sum')
```

## Interview tips
- `df.copy()` before modifying to avoid SettingWithCopyWarning
- `df.query()` is often more readable than boolean indexing
- `pd.cut()` and `pd.qcut()` for binning continuous variables
