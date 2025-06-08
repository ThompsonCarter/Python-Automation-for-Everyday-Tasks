import pandas as pd

df = pd.read_csv('data/raw_sales.csv')
df = df.dropna(subset=['sale_id', 'amount'])
df['amount'] = df['amount'].replace('[\$,]', '', regex=True).astype(float)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df.to_csv('data/clean_sales.csv', index=False)
print('Cleaned data saved.')