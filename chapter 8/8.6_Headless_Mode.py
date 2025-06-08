
# Headless Mode

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
