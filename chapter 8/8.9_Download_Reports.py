
# Download Reports

driver.get("https://example.com/reports")
links = driver.find_elements(By.CSS_SELECTOR, "a.download-link")

for link in links:
    href = link.get_attribute("href")
    driver.get(href)  # triggers download
    print("Downloaded", href.split("/")[-1])
