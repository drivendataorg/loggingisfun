import logging


logger = logging.getLogger(__name__)


def log_something():
    logger.debug("Wizzz!")
    logger.info("Magic!")
    logger.warning("Poof!")
