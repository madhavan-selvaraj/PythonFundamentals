from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def schedule(self, time):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email Sent:{message}")

    def schedule(self, time):
        print(f"Email schedule at :{time}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS Sent:{message}")

    def schedule(self, time):
        print(f"SMS schedule at :{time}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Push Notification Sent:{message}")

    def schedule(self, time):
        print(f"Push Notification schedule at :{time}")


user = EmailNotification()
user.send("Hello")
