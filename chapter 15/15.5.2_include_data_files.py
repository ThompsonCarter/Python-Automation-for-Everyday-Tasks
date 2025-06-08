# Include data files in the EXE
pyinstaller --onefile --add-data "templates/:templates/" app.py