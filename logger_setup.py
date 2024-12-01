import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

def set_logger():
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
        filename=LOG_FILE
    )
    logger = logging.getLogger("scrapper application")
    return logger

if __name__=="__main__":
    log=set_logger()
    log.info("hi")