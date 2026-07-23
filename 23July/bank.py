import logging

logger = logging.getLogger("GROOT")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("Bank.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class BankAccount:
    bank_name = "ABC bank"
    total_accounts = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1
        logger.info(
            f"Account created | Holder={self.account_holder} | Balance={self.balance}"
        )

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nBalance: Rs.{self.balance}"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            logger.warning("Balance cannot become negative")
            raise ValueError("Balance cannot become negative")

    def deposit(self, amount):
        if amount <= 0:
            logger.warning("Invalid deposit amount")
            raise ValueError("Invalid Amount")
        if not BankAccount.minimum_deposit(amount):
            logger.warning("Deposit below minimum amount")
            raise ValueError("Minimum deposit is Rs.500")
        self.balance += amount
        logger.info(
            f"{self.account_holder} deposited Rs.{amount}. Balance = Rs.{self.balance}"
        )
        return (
            f"Rs.{amount} is deposited successfully.\nCurrent Balance:Rs.{self.balance}"
        )

    def withdraw(self, amount):
        if amount <= 0:
            logger.warning("Invalid withdrawal amount")
            raise ValueError("Invalid Amount")
        if amount > self.balance:
            logger.warning("Invalid withdrawal")
            raise ValueError("Insufficient balance")
        self.balance -= amount
        logger.info(f"Money Withdraw-> Rs.{amount} is withdrawn")
        return (
            f"Rs.{amount} withdrawn successfully.\nCurrent Balance: Rs.{self.balance}"
        )

    @classmethod
    def change_bank_name(cls, bank_name):
        old_name = cls.bank_name
        cls.bank_name = bank_name
        logger.info(f"Bank name changed from {old_name} to {bank_name}")
        return "bank name changed successfully"

    @staticmethod
    def minimum_deposit(amount):
        return amount >= 500


if __name__ == "__main__":
    # Create accounts
    acc1 = BankAccount("Madhavan", 5000)
    acc2 = BankAccount("Rahul", 10000)

    print("Bank Name:", BankAccount.bank_name)
    print("Total Accounts:", BankAccount.total_accounts)

    print("-" * 40)

    # Deposit
    print(acc1.deposit(1000))

    print("-" * 40)

    # Withdraw
    print(acc1.withdraw(2000))

    print("-" * 40)

    # Change bank name
    print(BankAccount.change_bank_name("XYZ Bank"))
    print("Updated Bank Name:", BankAccount.bank_name)

    print("-" * 40)

    # Check minimum deposit
    print("Minimum Deposit (400):", BankAccount.minimum_deposit(400))
    print("Minimum Deposit (600):", BankAccount.minimum_deposit(600))

    print("-" * 40)

    # Invalid deposit
    try:
        print(acc1.deposit(200))
    except ValueError as e:
        print("Error:", e)

    print("-" * 40)

    # Invalid withdrawal
    try:
        print(acc1.withdraw(100000))
    except ValueError as e:
        print("Error:", e)

    print("-" * 40)

    # Negative balance during account creation
    try:
        acc3 = BankAccount("Arun", -500)
    except ValueError as e:
        print("Error:", e)

    print("-" * 40)

    # Final balance
    print(f"{acc1.account_holder}'s Balance: Rs.{acc1.balance}")
    print(f"{acc2.account_holder}'s Balance: Rs.{acc2.balance}")
