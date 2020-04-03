import logging
import os


LOG_LEVEL = os.getenv("LOGGINGISFUN_LOG_LEVEL", "WARNING")


def get_logger(level=LOG_LEVEL, propagate=True):
    logger = logging.getLogger(__package__)
    logger.setLevel(level)

    if len(logger.handlers) == 0:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)8s %(name)s | %(message)s')
        )
        stream_handler.setLevel(level)
        logger.addHandler(stream_handler)

    return logger


logger = get_logger()
logger.debug("debug")
logger.info("info")
logger.warning("warning")
