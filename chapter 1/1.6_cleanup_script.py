
# Folder Cleanup script (Project 1)
import os
from datetime import datetime, timedelta
from pathlib import Path
import shutil

DOWNLOADS = Path.home() / "Downloads"
ARCHIVE = Path.home() / "Downloads/Archive"
ARCHIVE.mkdir(exist_ok=True)

cutoff = datetime.now() - timedelta(days=30)

for file in DOWNLOADS.iterdir():
    if file.is_file() and datetime.fromtimestamp(file.stat().st_mtime) < cutoff:
        folder = ARCHIVE / file.stat().st_mtime.strftime("%Y-%m")
        folder.mkdir(exist_ok=True)
        shutil.move(str(file), folder / file.name)
        print(f"Archived {file.name} → {folder}")
    