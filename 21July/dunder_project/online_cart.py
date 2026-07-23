class shopping_cart:
    def __init__(self):
        self.items = {}

    def __add__(self, items):
        name, price = items
        self.items[name] = price
        return self

    def __sub__(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} is deleted successfully")
        else:
            print(f"{name} not found")
        return self

    def __getitem__(self, name):
        return self.items[name]

    def __setitem__(self, name, price):
        self.items[name] = price
        print(f"{name} is updated successfully")

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        result = ""
        for name, price in self.items.items():
            result += f"{name} : Rs.{price}\n"
        return result

    def __call__(self):
        return sum(self.items.values())

    def __iter__(self):
        return iter(self.items.items())


cart = shopping_cart()

cart = cart + ("Laptop", 65000)
cart = cart + ("Mouse", 1000)
cart = cart + ("Keyboard", 2000)
cart = cart - ("Laptop")
print(cart["Laptop"])
cart["Mouse"] = 3000
print("Mouse" in cart)
print(len(cart))
print(cart)
print(cart())
for name, price in cart:
    print(name, " ", price)
