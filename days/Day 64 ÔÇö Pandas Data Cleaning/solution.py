# Day 64 — Data Cleaning — SOLUTIONS
import pandas as pd
import re

def dedupe(df,subset): return df.drop_duplicates(subset=subset,keep='first')

def parse_dates(df,col):
    df=df.copy(); df[col]=pd.to_datetime(df[col])
    df['year']=df[col].dt.year; df['month']=df[col].dt.month
    df['day']=df[col].dt.day; df['day_of_week']=df[col].dt.day_name()
    return df

def remove_outliers(df,col):
    mean=df[col].mean(); std=df[col].std()
    return df[abs(df[col]-mean)<=3*std]

def clean_text(df,col):
    df=df.copy(); df[col]=df[col].str.lower().str.strip().str.replace(r'[^a-z0-9 ]','',regex=True)
    return df

def categorise_score(df):
    def grade(s):
        if s>=90: return 'A'
        elif s>=80: return 'B'
        elif s>=70: return 'C'
        elif s>=60: return 'D'
        else: return 'F'
    df=df.copy(); df['grade']=df['score'].apply(grade); return df

def merge_customer_orders(customers_df,orders_df):
    return customers_df.merge(orders_df,on='customer_id',how='left').fillna({'total':0})
