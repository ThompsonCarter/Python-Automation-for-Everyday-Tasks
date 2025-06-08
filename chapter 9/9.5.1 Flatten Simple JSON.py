import pandas as pd

items = fetch_items()
df = pd.json_normalize(items)
df.to_csv("items.csv", index=False)
print("Saved items.csv")