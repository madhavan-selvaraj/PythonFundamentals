from abc import ABC, abstractmethod


class InsufficientBalanceError(Exception):
    pass


def logger(func):
    def wrapper(self, amount):
        print("Transaction Started")
        result = func(self, amount)
        print("Transaction Completed")
        return result

    return wrapper


class BankAccount(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    @logger
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}Deposit succcessful \n")
        print(f"Current:{self.balance} ")

    @logger
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient Balance amount ")
        self.balance -= amount
        print(f"{amount} is deducted successfully")
        print(f"Current Balance:{self.balance}")


class CurrentAccount(BankAccount):
    @logger
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}Deposit succcessful \n")
        print(f"Current Balance:{self.balance}")

    @logger
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient Balance amount")
        self.balance -= amount
        print(f"{amount} is deducted successfully")
        print(f"Current Balance:{amount}")


savings = SavingsAccount("Madhavan", 10000)
current = CurrentAccount("Rahul", 20000)

try:
    print("------ Savings Account ------")

    savings.deposit(2000)

    savings.withdraw(3000)

    print()

    print("------ Current Account ------")

    current.deposit(1000)

    current.withdraw(7000)


except InsufficientBalanceError as error:
    print(error)
