
# Interacting with Elements

# Typing and Clicking
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, "button.login")

username.send_keys("user123")
password.send_keys("securepass")
login_btn.click()

# Dropdowns and Checkboxes
from selenium.webdriver.support.ui import Select

# Dropdown
select = Select(driver.find_element(By.ID, "country"))
select.select_by_visible_text("United States")

# Checkbox
checkbox = driver.find_element(By.ID, "agree")
if not checkbox.is_selected():
    checkbox.click()
