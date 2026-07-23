class ShopingCart:
    def __init__(self):
        self.products = {"Laptop": 1, "Mouse": 2, "Keyboard": 1}

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        return product in self.products

    def __getitem__(self, index):
        return self.products[index]

    def __setitem__(self, index, value):
        self.products[index] = value


cart = ShopingCart()
print(len(cart))
print("Laptop" in cart)
print(cart["Mouse"])
cart["Laptop"] = 3
print(cart.products)
