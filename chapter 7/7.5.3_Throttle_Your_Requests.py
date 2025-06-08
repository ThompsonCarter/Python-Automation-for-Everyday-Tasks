
import time
for url in urls:
    requests.get(url, headers=headers)
    time.sleep(2)  # two-second pause
