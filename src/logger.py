import logging 
import os
from datetime import datetime

# Define the log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"

# Create a logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings that these settings will be used to log the messages in the log file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging setup Started.....")
    logging.debug("This is a debug message.")
