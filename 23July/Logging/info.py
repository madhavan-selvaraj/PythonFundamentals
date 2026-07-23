import logging

logging.basicConfig(
    filename="info.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelno)s:%(levelname)s:%(name)s:%(message)s",
)


def add(a, b):
    result = a + b
    logging.info(f"Adding {a} and {b}")
    logging.info(f"Result = {result}")


def subtract(a, b):
    result = a - b
    logging.info(f"Subtracting {a} and {b}")
    logging.info(f"Result = {result}")


def multiply(a, b):
    result = a * b
    logging.info(f"Multiplying {a} and {b}")
    logging.info(f"Result = {result}")


def divide(a, b):
    if b == 0:
        logging.info("Cannot divide by zero")
    else:
        result = a / b
        logging.info(f"Dividing {a} by {b}")
        logging.info(f"Result = {result}")


add(10, 20)
subtract(30, 5)
multiply(4, 6)
divide(10, 2)
divide(10, 0)
