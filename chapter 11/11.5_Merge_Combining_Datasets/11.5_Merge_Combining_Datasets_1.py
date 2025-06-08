df1 = pd.read_csv('data/customers.csv')
df2 = pd.read_csv('data/sales.csv')
merged = pd.merge(df1, df2, on='customer_id', how='left')