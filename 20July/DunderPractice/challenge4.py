class Inventory:
    def __init__(self):
        self.products = {"Laptop": 10, "Mouse": 25, "Keyboard": 15, "Monitor": 8}

    def __len__(self):
        return len(self.products)

    def __contains__(self, item):
        return item in self.products

    def __getitem__(self, index):
        return self.products[index]

    def __setitem__(self, key, value):
        self.products[key] = value

    def __delitem__(self, key):
        del self.products[key]

    def __iter__(self):
        return iter(self.products)

    def __str__(self):
        return self.products


storage = Inventory()

print("1.Length of Inventory:", len(storage))
print("\n")
print("LAPTOP IN INVENTORY")
print("Laptop" in storage)
print("\n")
print("No of Laptops:", storage["Laptop"])
print("\nAFTER UPDATES INVENTORY")
storage["Monitor"] = 10
print(storage.products)
print("\nAFTER DELETE INVENTORY")
del storage["Keyboard"]
print(storage.products)
print("\n")
for product in storage:
    print(product)
