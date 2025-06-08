
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/monthly_sales.csv", parse_dates=["month"])
plt.figure(figsize=(10, 6))
plt.plot(df["month"], df["amount"], marker="o", linestyle="-")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.savefig("reports/figures/sales_trend.png")
plt.close()
