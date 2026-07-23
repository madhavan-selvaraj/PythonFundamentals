from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self):
        self.payment_history = []

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def show_history(self):
        print("\nPAYMENT HISTORY\n")
        for i in self.payment_history:
            print(i)


class CreditCard(Payment):
    def pay(self, amount):
        self.payment_history.append(f"Paid Rs.{amount} using Credit Card")
        print(f"Credit card payment successful Rs.{amount}")

    def refund(self, amount):
        self.payment_history.append(f"Refunded Rs.{amount} using Credit Card")
        print(f"Credit card refund successful Rs.{amount}")


class UPI(Payment):
    def pay(self, amount):
        self.payment_history.append(f"Paid Rs.{amount} using UPI")
        print(f"UPI payment successful Rs.{amount}")

    def refund(self, amount):
        self.payment_history.append(f"Refunded Rs.{amount} using UPI")
        print(f"UPI refund successful Rs.{amount}")


class PayPal(Payment):
    def pay(self, amount):
        self.payment_history.append(f"Paid Rs.{amount} using PayPal")
        print(f"PayPal payment successful Rs.{amount}")

    def refund(self, amount):
        self.payment_history.append(f"Refunded Rs.{amount} using PayPal")
        print(f"PayPal refund successful Rs.{amount}")


user = CreditCard()
user1 = PayPal()
user.pay(10000)
user.pay(2000)
user.refund(1000)
user1.pay(2000)
user1.refund(1000)
user.show_history()
user1.show_history()
