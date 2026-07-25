# Create a list of squares of numbers from 1 to 10.
list1 = [i**2 for i in range(1, 11)]
# print(list1)

# Create a list of cubes of numbers from 1 to 10.
list2 = [i * i * i for i in range(11)]
# print(list2)

# Create a list containing only even numbers from 1 to 20.
list3 = [i for i in range(1, 21) if i % 2 == 0]
# print(list3)

# Create a list containing only odd numbers from 1 to 20.
list4 = [i for i in range(1, 21) if i % 2 != 0]
# print(list4)

# Create a list containing the length of each word.
words = ["apple", "banana", "kiwi", "orange"]
len_list = [len(i) for i in words]
# print(len_list)

# Convert every name to lowercase.
names = ["John", "Alice", "Bob"]
lower_name = [i.lower() for i in names]
# print(lower_name)
