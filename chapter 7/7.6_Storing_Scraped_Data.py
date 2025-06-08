
import pandas as pd

data = []
# inside loop:
    data.append({"title": title, "price": price})
df = pd.DataFrame(data)
df.to_csv("products.csv", index=False)
print("Saved to products.csv")
