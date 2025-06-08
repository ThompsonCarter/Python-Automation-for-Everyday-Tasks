
# Waiting for Elements

# Implicit Wait
driver.implicitly_wait(10)  # seconds

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)
elem = wait.until(EC.presence_of_element_located((By.ID, "dashboard")))
