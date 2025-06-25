import logging
import os
from datetime import datetime

# Create 'logs' directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Create log file path with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] [Line:%(lineno)d] [%(name)s] - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Optional testing
if __name__ == "__main__":
    logging.info("Logger initialized successfully.")
    logging.debug("This is a debug message.")
