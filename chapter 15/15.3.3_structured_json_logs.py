import json, logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "time": self.formatTime(record),
            "level": record.levelname,
            "msg": record.getMessage()
        })

logging.basicConfig(handlers=[logging.StreamHandler()], level=logging.INFO)
logging.getLogger().handlers[0].setFormatter(JsonFormatter())