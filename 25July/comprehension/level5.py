# Create a dictionary mapping numbers from 1–5 to their squares.
dict1 = {i: i * i for i in range(1, 6)}
# print(dict1)

# Create a dictionary where:
# key → name ,value → length of the name
names = ["Alice", "Bob", "David"]
dict2 = {name: len(name) for name in names}
# print(dict2)

# Create a dictionary where:
# key → number,value → "Even" or "Odd"
numbers = [1, 2, 3, 4, 5]
dict3 = {num: "Even" if num % 2 == 0 else "Odd" for num in numbers}
print(dict3)
