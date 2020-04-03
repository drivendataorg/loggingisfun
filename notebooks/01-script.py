import logging
import os
level = "DEBUG"
os.environ["LOGGINGISFUN_LOG_LEVEL"] = level


from loggingisfun import wizard
wizard.log_something()


from loggingisfun import barbarian
barbarian.log_something()


# uh-oh a demon
from loggingisfun import demon
demon.log_something()  # it's cursed!
wizard.log_something()  # it curses everyone!
barbarian.log_something()  # even the barbarian?!


# can basicConfig break what it broke?
logging.basicConfig(handlers=None)
wizard.log_something()  # no!
logging.root.handlers  # there are still handlers?!


logging.root.handlers = []  # can we just do this?
wizard.log_something()  # yes!


# another solution, do not propagate our logs to root logger
logger = logging.getLogger("loggingisfun")
logger.propagate = False
wizard.log_something()
