
# Multi-Step Form Submission

driver = webdriver.Chrome()
driver.get("https://example.com/survey")

# Page 1
driver.find_element(By.NAME, "age").send_keys("30")
driver.find_element(By.NAME, "next").click()

# Wait and fill Page 2
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "q1")))
driver.find_element(By.ID, "q1_option2").click()
driver.find_element(By.ID, "submit").click()

print("Survey submitted")
driver.quit()
