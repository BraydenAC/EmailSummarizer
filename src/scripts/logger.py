import logging
from pathlib import Path
from datetime import datetime

#Manual config
logging_level = logging.DEBUG # <-- Need to remember to use this across all levels for consistency.
logger = logging.getLogger("logger_main")
logger.setLevel(logging_level)

#Get file path
src_folder = Path(__file__).resolve().parent.parent
logs_folder = src_folder.parent / ".logs"
logs_folder.mkdir(exist_ok=True)
#Make filename and join
log_file_name = datetime.now().strftime("%m-%d_%H:%M:%S")
log_file = logs_folder / f"{log_file_name}.log"

#create File handler
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging_level)

#Create formatter
formatter = logging.Formatter(
    '%(asctime)s|%(levelname)7s|%(name)s: %(message)s',
    datefmt = '%H:%M:%S'
)
file_handler.setFormatter(formatter)

if logger.hasHandlers:
    logger.handlers.clear()
logger.addHandler(file_handler)