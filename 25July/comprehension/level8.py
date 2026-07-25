# Create a dictionary where:
# key = word
# value = number of vowels in that word.
words = ["apple", "banana", "kiwi", "orange", "grape"]

dict = {word: sum(1 for ch in word if ch.lower() in "aeiou") for word in words}
# print(dict)

# Create a list containing only the digits.
text = "Python123Programming456"

list = [ch for ch in text if ch.isdigit()]
# print(list)

# Create a list of all pairs (i, j) where:
# i ranges from 1 to 3
# j ranges from 1 to 3

list2 = [(i, j) for i in range(1, 4) for j in range(1, 4)]
# print(list2)

# Extract only the even numbers using a nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

even_list = [num for row in matrix for num in row if num % 2 == 0]
# print(even_list)


# Create a dictionary containing only the students with marks ≥ 50.
students = {"Alice": 85, "Bob": 42, "Charlie": 91, "David": 55}

dict2 = {name: mark for name, mark in students.items() if mark >= 50}
# print(dict2)
