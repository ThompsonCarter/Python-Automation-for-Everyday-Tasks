
# Task Scheduler script (Project 2)
import schedule, time
from cleanup import run_cleanup  # Assuming cleanup.py exists with a run_cleanup function

schedule.every().sunday.at("03:00").do(run_cleanup)

print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(30)
    