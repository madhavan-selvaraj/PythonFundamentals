# Create a list of numbers from 1–30 that are divisible by 3
list1 = [num for num in range(1, 31) if num % 3 == 0]
# print(list1)

# Create a list containing only positive numbers.
numbers = [4, -2, 7, -5, 9, -1]
list2 = [num for num in numbers if num > 0]
# print(list2)

# Create a list containing numbers greater than 10.
numbers = [5, 12, 3, 18, 7, 25]
list3 = [num for num in numbers if num > 10]
# print(list3)

# Create a list of words whose length is greater than 3.
words = ["cat", "elephant", "dog", "tiger"]
list4 = [word for word in words if len(word) > 3]
# print(list4)

# Create a list containing only the vowels.
text = "Python Programming"
list5 = [char for char in text if char.lower() in "aeiou"]
# print(list5)
