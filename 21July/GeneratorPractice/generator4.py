def fibbinoci_numbers(num1):
    n1 = 0
    n2 = 1
    for _i in range(10):
        yield (n1)
        n1, n2 = n2, n1 + n2


def prime_numbers(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            yield i


def factorial(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i


for i in factorial(30):
    print(i)
