import schedule, time

def job():
    print("Running job at", time.strftime("%X"))

schedule.every(10).minutes.do(job)
schedule.every().day.at("14:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)