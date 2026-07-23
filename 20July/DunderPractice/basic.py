class Student:
    def __new__(cls):
        print("Object Created")
        return super().__new__(cls)

    def __init__(self):
        print("Student Initialized")


S1 = Student()
S2 = Student()


class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"


c = car("Toyatta", "Supra")
print(c)


class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f"car('{self.brand}','{self.model}')"


c = car("Toyato", "Camry")
print(repr(c))


class book:
    def __del__(self):
        print("Object Deleted")


s = book()
del s


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


songs = Playlist(["A", "B", "C", "D"])
print(len(songs))
