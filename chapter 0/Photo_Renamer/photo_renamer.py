
from pathlib import Path
import exifread, re, shutil

SRC = Path.home() / "Pictures/Unsorted"
DST = Path.home() / "Pictures/Renamed"
DST.mkdir(exist_ok=True)

def rename(file, counter):
    with open(file, "rb") as f:
        tags = exifread.process_file(f, stop_tag="DateTimeOriginal", details=False)
    date = str(tags["EXIF DateTimeOriginal"])[:10].replace(":", "-")
    new = f"{date}_Bali_{counter:04}.jpg"
    shutil.copy(file, DST / new)
    print(f"{file.name} → {new}")

for i, pic in enumerate(sorted(SRC.glob("*.JPG")), 1):
    rename(pic, i)
