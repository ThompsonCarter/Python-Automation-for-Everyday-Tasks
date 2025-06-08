
import csv
from collections import defaultdict

totals = defaultdict(float)
with open("sales.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        amount = float(row["amount"])
        totals[product] += amount

for product, total in totals.items():
    print(product, "→", total)
