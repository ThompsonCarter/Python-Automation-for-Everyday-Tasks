
# Element-Locator Strategies

from selenium.webdriver.common.by import By

# By ID
elem = driver.find_element(By.ID, "username")

# By name
elem = driver.find_element(By.NAME, "password")

# By CSS selector
elem = driver.find_element(By.CSS_SELECTOR, ".login-btn")

# By XPath
elem = driver.find_element(By.XPATH, "//button[text()='Submit']")
