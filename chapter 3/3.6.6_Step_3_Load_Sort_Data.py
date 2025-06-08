# Code for loading and sorting data
import pandas as pd

csv_path = path
df = pd.read_csv(csv_path)
df = df.sort_values("Region", ascending=False)

report = pathlib.Path("Report_" + pd.Timestamp.today().strftime("%Y%m%d") + ".xlsx")
df.to_excel(report, index=False)
print("Report saved:", report)