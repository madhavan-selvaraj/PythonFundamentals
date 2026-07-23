class Transaction:
    def __init__(
        self,
        transaction_id,
        account_number,
        transaction_type,
        amount,
        date_time,
        balance,
    ):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.date_time = date_time
        self.balance = balance

    def __str__(self):
        return (
            f"Transaction ID   : {self.transaction_id}\n"
            f"Account Number   : {self.account_number}\n"
            f"Transaction Type : {self.transaction_type}\n"
            f"Amount           : {self.amount}\n"
            f"Date & Time      : {self.date_time}\n"
            f"Balance          : {self.balance}\n\n\n"
        )


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return self

    def transaction_history(self):
        yield from self.transactions


history = TransactionHistory()

history.add_transaction(
    Transaction("TXN001", "ACC1001", "Deposit", 5000, "21-Jul-2026 10:30 AM", 5000)
)

history.add_transaction(
    Transaction("TXN002", "ACC1001", "Withdrawal", 1500, "22-Jul-2026 10:30 AM", 3500)
)

history.add_transaction(
    Transaction("TXN003", "ACC1001", "Transfer", 1000, "23-Jul-2026 10:30 AM", 2500)
)

for transaction in history.transaction_history():
    print(transaction)
