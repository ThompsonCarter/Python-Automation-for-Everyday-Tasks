# Step 1: Read & Process Data
import pandas as pd
from pathlib import Path

data_file = Path("data/sales_2025-05.csv")
df = pd.read_csv(data_file)

# Quick summary
summary = df.groupby("Region")["Amount"].sum().reset_index()
summary_file = Path("output/summary_2025-05.csv")
summary.to_csv(summary_file, index=False)
print("Summary saved:", summary_file)
