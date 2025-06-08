def main():
    items = fetch_items()
    df = pd.json_normalize(items)
    df.to_csv("output/items.csv", index=False)
    df.to_sql("items", engine, if_exists="replace")
    print("Pipeline complete.")

if __name__ == "__main__":
    main()