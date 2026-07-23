import logging

logger = logging.getLogger("mad")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelno)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("debug.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b}")
    logger.debug(f"Result = {result}")


def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} and {b}")
    logger.debug(f"Result = {result}")


def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b}")
    logger.debug(f"Result = {result}")


def divide(a, b):
    if b == 0:
        logger.debug("Cannot divide by zero")
    else:
        result = a / b
        logger.debug(f"Dividing {a} by {b}")
        logger.debug(f"Result = {result}")


add(10, 20)
subtract(30, 5)
multiply(4, 6)
divide(10, 2)
divide(10, 0)
