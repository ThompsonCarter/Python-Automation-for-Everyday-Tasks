
base = "https://example.com/products?page="
for page in range(1, 6):
    resp = requests.get(base + str(page))
    soup = BeautifulSoup(resp.text, "html.parser")
    # extract items
