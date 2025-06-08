
import matplotlib.pyplot as plt

df = pd.read_csv("products.csv")
plt.hist(df["price"], bins=20)
plt.title("Price distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()
