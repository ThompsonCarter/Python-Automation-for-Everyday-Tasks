df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['price'] = df['price'].astype(float)