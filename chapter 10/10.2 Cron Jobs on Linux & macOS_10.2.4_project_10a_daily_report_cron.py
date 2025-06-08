0 6 * * * /home/user/.venv/bin/python /home/user/automation/daily_report.py >> /home/user/automation/logs/report.log 2>&1
# Test: temporarily change to run every minute:
* * * * * /home/user/.venv/bin/python /home/user/automation/daily_report.py >> /home/user/automation/logs/report.log 2>&1
# Verify with: tail -f logs/report.log