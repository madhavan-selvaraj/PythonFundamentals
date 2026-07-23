import logging

logger = logging.getLogger("groot")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(levelname)s:%(levelno)s:%(name)s:%(module)s:%(message)s"
)

file_handler = logging.FileHandler("prime.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


n = int(input("Enter the limit: "))

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        logger.info(num)
