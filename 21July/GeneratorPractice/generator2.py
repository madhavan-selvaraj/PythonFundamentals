def one_char(text):
    yield from text


def one_word(text):
    yield from text.split()


def reverse_char(str):
    for i in range(len(str) - 1, -1, -1):
        yield str[i]


def vowels(str):
    for i in str.lower():
        if i in ["a", "e", "i", "o", "u"]:
            yield i


def consonants(str):
    for i in str.lower():
        if i not in ["a", "e", "i", "o", "u"]:
            yield i
