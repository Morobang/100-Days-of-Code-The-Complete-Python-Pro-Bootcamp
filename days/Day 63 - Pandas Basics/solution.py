# Day 63 — Pandas Basics — SOLUTIONS
import pandas as pd

def explore(df):
    return {'shape':df.shape,'columns':list(df.columns),'dtypes':dict(df.dtypes.astype(str)),'nulls':dict(df.isnull().sum())}

def top_scorers(df,n):
    return df[df['score']>80].sort_values('score',ascending=False).head(n)

def add_bmi(df):
    df=df.copy(); df['bmi']=round(df['weight_kg']/df['height_m']**2,1); return df

def clean(df):
    df=df.dropna(subset=['name'])
    for col in df.select_dtypes('number').columns: df[col]=df[col].fillna(df[col].median())
    return df

def genre_summary(df):
    return df.groupby('genre').agg(count=('title','count'),avg_price=('price','mean')).reset_index()

def monthly_sales(df):
    df['month']=pd.to_datetime(df['date']).dt.to_period('M')
    return df.pivot_table(index='month',columns='product',values='amount',aggfunc='sum')
