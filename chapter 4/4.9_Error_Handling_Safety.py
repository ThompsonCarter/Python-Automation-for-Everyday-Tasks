
import pyautogui

# Enable the fail-safe
pyautogui.FAILSAFE = True

# Wrap risky code
try:
    pyautogui.click(10000, 10000)  # Off-screen, triggers fail-safe
except pyautogui.FailSafeException:
    print("Aborted by moving mouse to corner.")

# Add a small pause between actions
pyautogui.PAUSE = 0.5
