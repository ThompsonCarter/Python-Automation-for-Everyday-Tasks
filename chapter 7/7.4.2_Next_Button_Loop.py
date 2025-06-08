
url = "https://example.com/products"
while url:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    # extract products...
    next_link = soup.find("a", text="Next")
    url = next_link.get("href") if next_link else None
