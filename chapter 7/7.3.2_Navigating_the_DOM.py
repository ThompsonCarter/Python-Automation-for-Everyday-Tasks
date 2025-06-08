
title = soup.find("h1").get_text(strip=True)
print("Title:", title)

links = soup.find_all("a", class_="product-link")
for a in links:
    print(a.get("href"), "-", a.text)
