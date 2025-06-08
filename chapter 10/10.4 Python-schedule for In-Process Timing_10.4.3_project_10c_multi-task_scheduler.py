import schedule, time
from tasks import report, backup

schedule.every().day.at("06:00").do(report.generate)
schedule.every().friday.at("23:00").do(backup.run)

print("Scheduler started.")
while True:
    schedule.run_pending()
    time.sleep(30)