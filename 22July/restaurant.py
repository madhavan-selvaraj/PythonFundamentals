import time
from abc import ABC, abstractmethod


class RestuarantClosedError(Exception):
    pass


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        preparation_time = end_time - start_time
        print(f"Preparation Time:{preparation_time:.0f}min\n")
        return result

    return wrapper


class Restaurant(ABC):
    def __init__(self, restaurant_name, is_open):
        self.restaurant_name = restaurant_name
        self.is_open = is_open

    @abstractmethod
    def prepare_order(self, order):
        pass

    @abstractmethod
    def show_menu(self):
        pass


class PizzaHut(Restaurant):
    @timer
    def prepare_order(self, order):
        if not self.is_open:
            raise RestuarantClosedError("Restaurant is Closed\n")
        print(f"Preparing {order}")
        time.sleep(3)
        print(f"{order} is Ready")

    def show_menu(self):
        print("\n PIZZA HUT MENU")
        print("1.Veg Pizza")
        print("2.Cheese Pizza")


class KFC(Restaurant):
    @timer
    def prepare_order(self, order):
        if not self.is_open:
            raise RestuarantClosedError("Restaurant is Closed\n")
        print(f"Preparing {order}")
        time.sleep(4)
        print(f"{order} is Ready")

    def show_menu(self):
        print("\n KFC MENU")
        print("1.Fried Chicken")
        print("2.Burger")


class DominoS(Restaurant):
    @timer
    def prepare_order(self, order):
        if not self.is_open:
            raise RestuarantClosedError("Restaurant is Closed\n")
        print(f"Preparing {order}")
        time.sleep(5)
        print(f"{order} is Ready")

    def show_menu(self):
        print("\n DOMINO'S MENU")
        print("1.Veg Pizza")
        print("2.Cheese Pizza")


pizza = PizzaHut("Pizza Hut", True)
kfc = KFC("KFC", False)
dominos = DominoS("Domino's", True)

restaurants = [pizza, kfc, dominos]

for restaurant in restaurants:
    print(restaurant.restaurant_name)

    restaurant.show_menu()

    try:
        restaurant.prepare_order("Special Order")

    except RestuarantClosedError as e:
        print(e)
