class money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return money(self.amount + other.amount)

    def __sub__(self, other):
        return money(self.amount - other.amount)

    def __mul__(self, other):
        return money(self.amount * other.amount)


m1 = money(500)
m2 = money(700)
print((m1 + m2).amount)
print((m1 - m2).amount)
print((m1 * m2).amount)


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __eq__(self, others):
        return self.roll_no == others.roll_no


s1 = Student("Alex", 101)
s2 = Student("John", 101)
print(s1 == s2)


class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary


e1 = employee("Arox", 5000)
e2 = employee("Brox", 6000)
print(e1 < e2)


class products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


p1 = products("Biscuit", 40)
p2 = products("Milk", 30)
print(p1 > p2)


class wallet:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0


w1 = wallet(0)
print(bool(w1))


class Tempreture:
    def __init__(self, value):
        self.value = value

    def __abs__(self):
        return abs(self.value)


temp = Tempreture(-25)
print(abs(temp))
