from flask import Flask, render_template, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
import tasks

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

# Schedule tasks
scheduler.add_job(tasks.daily_report, 'cron', hour=6, id='daily_report')
scheduler.add_job(tasks.cleanup, 'cron', day_of_week='mon', hour=3, id='weekly_cleanup')

@app.route("/")
def index():
    jobs = scheduler.get_jobs()
    return render_template("index.html", jobs=jobs)

@app.route("/run/<job_id>")
def run_job(job_id):
    job = scheduler.get_job(job_id)
    job.func()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=5000)