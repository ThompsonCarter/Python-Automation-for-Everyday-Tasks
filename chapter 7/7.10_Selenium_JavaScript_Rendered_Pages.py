
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/dynamic")
content = driver.page_source
# then parse with BeautifulSoup
