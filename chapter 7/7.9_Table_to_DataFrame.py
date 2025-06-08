
import pandas as pd

rows = []
for tr in soup.select("#stats tr"):
    rows.append([td.text for td in tr.find_all(["td","th"])])
df = pd.DataFrame(rows[1:], columns=rows[0])
df.to_excel("stats.xlsx", index=False)
print("Excel file created.")
