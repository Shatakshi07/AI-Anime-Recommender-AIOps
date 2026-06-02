from datetime import datetime
import logging
import os

LOGS_DIR = "logs"
os.makdirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S,')}.log")

logging.basicConfig(
    filename = LOG_FILE,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO    #INFO, WARNING, ERROR
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger