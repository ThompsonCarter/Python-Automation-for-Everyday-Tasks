import pandas as pd

reader = pd.read_csv('data/logs.csv', chunksize=500000, parse_dates=['timestamp'])
counts = {}
for chunk in reader:
    cnt = chunk['level'].value_counts().to_dict()
    for lvl, c in cnt.items():
        counts[lvl] = counts.get(lvl, 0) + c

pd.DataFrame(list(counts.items()), columns=['level', 'count']).to_csv('output/log_counts.csv', index=False)