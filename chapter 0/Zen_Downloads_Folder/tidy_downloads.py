
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from datetime import datetime, timedelta
import shutil, time

DOWNLOADS = Path.home() / "Downloads"
AGE = timedelta(days=7)

class Mover(FileSystemEventHandler):
    def on_created(self, event):
        self.organize()

    def organize(self):
        for file in DOWNLOADS.iterdir():
            if file.is_file() and datetime.now() - datetime.fromtimestamp(file.stat().st_mtime) > AGE:
                dest = DOWNLOADS / f"{file.stat().st_mtime:%Y}/{file.stat().st_mtime:%m}"
                dest.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file), dest / file.name)
                print(f"Moved {file.name} → {dest}")

if __name__ == "__main__":
    handler = Mover(); handler.organize()          # initial sweep
    Observer().schedule(handler, DOWNLOADS, recursive=False)
    Observer().start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        Observer().stop()
