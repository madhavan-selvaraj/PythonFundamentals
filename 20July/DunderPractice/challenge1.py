class Bank:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def __str__(self):
        return f"ACCOUNT HOLDER:{self.name},ACCOUNT NUMBER:{self.acc_no},BALANCE:$.{self.balance}"

    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance

    def __eq__(self, other):
        return self.acc_no == other.acc_no


user1 = Bank("Madhavan", 1001, 6000)
user2 = Bank("ARun", 1002, 8000)
print(user1)
print(user1 + user2)
print(user1 - user2)
print(user1 == user2)
