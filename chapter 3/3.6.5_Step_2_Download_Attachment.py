# Code for downloading attachment
import pathlib

TEMP = pathlib.Path("temp")
TEMP.mkdir(exist_ok=True)

if msg:
    for att in msg.attachments:
        if att.filename.endswith(".csv"):
            path = TEMP / att.filename
            with open(path, "wb") as f:
                f.write(att.payload)
            print("Saved", path)
            break
else:
    print("No report email found.")
    exit()