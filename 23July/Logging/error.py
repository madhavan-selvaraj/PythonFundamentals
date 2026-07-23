import logging

logger = logging.getLogger("groot")
logger.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(levelname)s:%(levelno)s:%(name)s:%(module)s:%(message)s"
)

file_handler = logging.FileHandler("error.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


try:
    num = 10 / 0
except ZeroDivisionError:
    logger.error("Cannot divide by zero")
