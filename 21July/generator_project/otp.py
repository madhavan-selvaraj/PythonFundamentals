import random


def otp_generator():
    while True:
        OTP = random.randint(100000, 1000000)
        yield OTP


generator = otp_generator()


print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
