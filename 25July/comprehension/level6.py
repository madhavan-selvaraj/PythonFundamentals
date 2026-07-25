# Create a set containing unique numbers.
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
set1 = {num for num in numbers}
# print(set1)

# Create a set containing the lengths of all words.
words = ["apple", "banana", "apple", "kiwi"]
set2 = {f"{word}-{len(word)}" for word in words}
# print(set2)
