clients = pd.read_csv('data/clients.csv')
sales = pd.read_csv('data/clean_sales.csv')
report = clients.merge(sales, on='client_id', how='inner')
report.to_excel('output/client_sales.xlsx', index=False)