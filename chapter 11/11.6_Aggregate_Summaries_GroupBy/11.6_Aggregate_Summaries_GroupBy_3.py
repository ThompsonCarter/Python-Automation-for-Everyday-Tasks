df['month'] = df['sale_date'].dt.to_period('M')
monthly = df.groupby('month')['amount'].sum().reset_index()
monthly.to_csv('output/monthly_sales.csv', index=False)