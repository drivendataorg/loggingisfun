import logging
import os


LOG_LEVEL = os.getenv("LOGGINGISFUN_LOG_LEVEL", "WARNING")
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

def log_something():
    logger.debug("Nyaaa")
    logger.info("Gobblegobblegobble")
    logger.warning("Blech")
