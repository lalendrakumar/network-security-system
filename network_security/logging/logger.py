import logging
import os
from datetime import datetime

#1. Log file ka naam → Time ke sath
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Logs folder banana
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

# 3. Final log file path
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# 4. Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

