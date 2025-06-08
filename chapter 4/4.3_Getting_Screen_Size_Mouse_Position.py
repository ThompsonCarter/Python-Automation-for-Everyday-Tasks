
import pyautogui

# Get screen size
width, height = pyautogui.size()
print(width, height)  # e.g., 1920 1080

# Get current mouse position
x, y = pyautogui.position()
print(x, y)  # where your mouse currently sits
