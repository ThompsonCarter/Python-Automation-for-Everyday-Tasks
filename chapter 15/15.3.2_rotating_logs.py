from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("logs/app.log", maxBytes=1_000_000, backupCount=5)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(handler)