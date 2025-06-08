chunks = []
for chunk in pd.read_csv('big.csv', chunksize=100000):
    chunks.append(chunk[chunk['flag'] == True])
result = pd.concat(chunks)