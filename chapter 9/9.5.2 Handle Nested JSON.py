nested = {
  "order": {
    "id": 123, "customer": {"name": "Alice", "tier": "gold"},
    "items": [{"sku": "A1", "qty":2}, {"sku": "B2", "qty":1}]
  }
}
df = pd.json_normalize(nested,
       record_path=["order", "items"],
       meta=[["order","id"], ["order","customer","name"]])