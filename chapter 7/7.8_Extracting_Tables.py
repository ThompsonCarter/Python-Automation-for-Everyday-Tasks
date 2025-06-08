
table = soup.find("table", id="stats")
rows = table.find_all("tr")
for tr in rows:
    cols = [td.text for td in tr.find_all(["td","th"])]
    print(cols)
