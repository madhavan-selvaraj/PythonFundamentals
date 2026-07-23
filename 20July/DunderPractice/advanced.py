class Library:
    def __init__(self):
        self.books = ["ABC", "DEF", "GHI"]

    def __getitem__(self, index):
        return self.books[index]

    def __setitem__(self, index, value):
        self.books[index] = value

    def __delitem__(self, index):
        del self.books[index]

    def __contains__(self, book):
        return book in self.books


b1 = Library()
b1[2] = "Python"
print("AB" in b1)
print(b1.books)


class numbers:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        raise StopIteration


for i in numbers():
    print(i)


class Calculator:
    def __call__(self, x, y):
        return x + y


calc = Calculator()
print(calc(10, 20))


class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        print("Opening file")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        print("Closing file")
        self.file.close()


with FileHandler("sample.txt") as f:
    print("working")
    f.write("Hello world")
