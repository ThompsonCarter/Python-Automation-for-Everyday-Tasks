
# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")

# Focus on a specific region
region = (0, 0, 800, 600)  # x, y, width, height
pyautogui.screenshot("crop.png", region=region)

# Search for an on-screen image
button = pyautogui.locateOnScreen("submit_button.png", confidence=0.9)
if button:
    pyautogui.click(button)
