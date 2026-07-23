def count(n):  # Create a generator that yields numbers from 1 to n.
    yield from range(1, n + 1)


def count_down(n):  # Yield numbers from n down to 1.
    while n > 0:
        yield n
        n -= 1


def even_num(num):  # Yield all even numbers from 1 to n.
    yield from range(2, num + 1, 2)


def odd_num(n):
    yield from range(1, n, 2)


def square_num(n):  # Yield the square of numbers from 1 to n.
    for i in range(1, n + 1):
        yield i, i**2


def cube_num(n):  # Yield the square of numbers from 1 to n.
    for i in range(1, n + 1):
        yield i, i * i * i


def mul(n):  # Yield the multiplication table of a given number.
    for i in range(1, 11, 1):
        yield i, i * n


def alpha_gen():  # Yield letters from 'A' to 'Z'. &  Yield letters from 'a' to 'z'.
    for i in range(26):
        yield chr(i + 65), chr(i + 97)


def reverse_alpha():  # Yield letters from 'Z' to 'A'. & Yield letters from 'z' to 'a'.
    for i in range(25, -1, -1):
        yield chr(i + 65), chr(i + 97)
