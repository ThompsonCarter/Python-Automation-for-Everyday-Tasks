$action = New-ScheduledTaskAction -Execute "C:\Python39\python.exe" -Argument "C:\scripts\daily_report.py"
$trigger = New-ScheduledTaskTrigger -Daily -At 6am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "DailyReport" -Description "Run daily report script" 