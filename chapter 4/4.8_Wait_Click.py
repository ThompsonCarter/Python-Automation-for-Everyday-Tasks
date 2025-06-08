
import pyautogui, time

# Wait for the popup to appear and click it
while True:
    loc = pyautogui.locateOnScreen("popup.png", confidence=0.8)
    if loc:
        pyautogui.click(pyautogui.center(loc))
        print("Clicked popup")
        break
    time.sleep(1)
