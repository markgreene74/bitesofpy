import logging
from typing import Callable

DEBUG = "10"
INFO = "20"
WARNING = "30"
ERROR = "40"
CRITICAL = "50"


def log_it(level: Callable, msg: str) -> None:
    logger = logging.getLogger('pybites_logger')
    logger.log(int(level), msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")