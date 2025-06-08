import schedule, time
from pipeline import main

schedule.every().hour.do(main)
while True:
    schedule.run_pending()
    time.sleep(60)