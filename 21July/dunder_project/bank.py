class Bank:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def __str__(self):
        return str((self.account_no, self.name, self.balance))

    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance


acc1 = Bank(101, "ABC", 300)
acc2 = Bank(102, "DEF", 300)
print(acc1 + acc2)
print(acc1 - acc2)
acc1 = acc1 + 500
acc1 = acc1 - 200
print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
print(acc2)
