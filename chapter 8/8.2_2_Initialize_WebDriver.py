
# Initialize WebDriver

from selenium import webdriver

# Chrome example
driver = webdriver.Chrome()  # assumes chromedriver in PATH

# Firefox example
# driver = webdriver.Firefox(executable_path="path/to/geckodriver")

driver.get("https://example.com")
print("Title:", driver.title)
driver.quit()
