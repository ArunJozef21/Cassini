# utils/logger.py
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler("logs/api_test.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger