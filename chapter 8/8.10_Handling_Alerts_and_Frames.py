
# Handling Alerts & Frames

# Alerts
alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # or alert.dismiss()

# iFrames
frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(frame)
# interact inside iframe
driver.switch_to.default_content()
