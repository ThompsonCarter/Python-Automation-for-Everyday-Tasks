df.rename(columns={'qty': 'quantity'}, inplace=True)
df.drop(columns=['unnecessary_col'], inplace=True)