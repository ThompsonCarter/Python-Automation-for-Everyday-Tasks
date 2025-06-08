import pandas as pd

csv_df = pd.read_csv('data/sales.csv')
excel_df = pd.read_excel('data/clients.xlsx', sheet_name='Clients')
json_df = pd.read_json('data/config.json')

print(csv_df.shape, excel_df.shape, json_df.shape)