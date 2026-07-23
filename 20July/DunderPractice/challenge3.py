class Matrix:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return self.values + other.values

    def __sub__(self, other):
        return self.values - other.values

    def __mul__(self, other):
        return self.values * other.values

    def __str__(self):
        return self.values


m1 = Matrix(10)
m2 = Matrix(20)

print(m1 + m2)
print(m1 - m2)
print(m1 * m2)
print(m1)
