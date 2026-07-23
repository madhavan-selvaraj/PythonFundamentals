import logging

logger = logging.getLogger("groot")
logger.setLevel(logging.CRITICAL)

formatter = logging.Formatter(
    "%(levelname)s:%(levelno)s:%(name)s:%(module)s:%(message)s"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

database_connected = False

if not database_connected:
    logging.critical("Database connection failed. Application shutting down.")
