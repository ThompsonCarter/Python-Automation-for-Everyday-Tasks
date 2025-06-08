# Code for file archiving
from pathlib import Path
from datetime import datetime, timedelta
import shutil

LOG_DIR = Path("logs")
ARCHIVE = Path("archive")
ARCHIVE.mkdir(exist_ok=True)
cutoff = datetime.now() - timedelta(days=7)

for log in LOG_DIR.glob("*.log"):
    if datetime.fromtimestamp(log.stat().st_mtime) < cutoff:
        dest = ARCHIVE / log.stat().st_mtime.strftime("%Y-%m")
        dest.mkdir(exist_ok=True)
        shutil.move(str(log), dest / log.name)
        print(f"Archived {log.name}")