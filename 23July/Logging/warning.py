import logging

logger = logging.getLogger("groot")
logger.setLevel(logging.WARNING)

formatter = logging.Formatter(
    "%(levelname)s:%(levelno)s:%(name)s:%(module)s:%(message)s"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

age = 15

if age < 18:
    logger.warning("User is under 18")
else:
    print("Access Granted")
