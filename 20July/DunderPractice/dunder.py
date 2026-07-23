# -----OBJECT INITIALIZATION METHOD-----------
class student:
    def __new__(cls):
        print("Craeting object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing Object")


s = student()


class student:
    def __init__(self, name):
        self.name = name


s = student("John")
print(s.name)


class student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


s = student("Alicent")
print(s)


class student:
    def __repr__(self):
        return "Student()"


s = student()
print(repr(s))


class number:
    def __init__(self, value):
        self.value = value

    def __pow__(self, other):
        return number(self.value**other.value)


n1 = number(10)
n2 = number(60)
result = n1**n2
print(result.value)


class student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = student(9)
s2 = student(80)
print(s1 > s2)


class team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


t = ["A", "B", "C"]
print(len(t))


class numbers:
    def __init__(self):
        self.data = [10, 20, 30]

    def __getitem__(self, index):
        return self.data[index]


n = numbers()
print(n[0])


class number:
    def __init__(self):
        self.data = [10, 20, 30]

    def __setitem__(self, index, value):
        self.data[index] = value


n = number()
n[1] = 100
print(n.data)


# class team:
#     def __init__(self):
#         self.players = ["John", "Mike"]

#     def __contains__(self, player):
#         return player in self.players


# t = team()
# print("john" in t)


class counter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 3:
            value = self.num
            self.num += 1
            return value
        raise StopIteration


for i in counter():
    print(i)


class Calculator:
    def __call__(self, x, y):
        return x * y


calc = Calculator()
print(calc(6, 6))


class demo:
    def __enter__(self):
        print("ENTRY")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("EXIT")


with demo():
    print("WITH")


class student:
    def __getattr__(self, name):
        return f"{name} not found"


s = student()
print(s.age)


class student:
    def __setattr__(self, name, value):
        print(f"settting {name}={value}")
        super().__setattr__(name, value)


s = student()
s.name = "ALice"
