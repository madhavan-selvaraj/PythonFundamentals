def my_list(numbers):
    for i in numbers:
        if i > 0:
            yield i


def positive_list(numbers):
    for i in numbers:
        if i > 0:
            yield i


def negetive_list(numbers):
    for i in numbers:
        if i < 0:
            yield i


def even_list(numbers):
    for i in numbers:
        if i % 2 == 0:
            yield i


def unique_list(numbers):
    seen = set()
    for i in numbers:
        if i not in seen:
            seen.add(i)
            yield i
