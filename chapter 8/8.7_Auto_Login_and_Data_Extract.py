
# Auto-Login and Data Extract

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DEMO_URL")
user = os.getenv("USER")
pwd = os.getenv("PASS")

driver = webdriver.Chrome()
driver.get(url)

# Locate and fill login form
driver.find_element(By.ID, "email").send_keys(user)
driver.find_element(By.ID, "password").send_keys(pwd)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for dashboard
driver.implicitly_wait(10)
welcome = driver.find_element(By.ID, "welcome-message").text
print("Logged in: ", welcome)

driver.quit()
