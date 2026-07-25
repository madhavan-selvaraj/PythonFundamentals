# Create a list where: Even → "Even" Odd → "Odd"
numbers = range(1, 11)
list1 = [f"{num}-even" if num % 2 == 0 else f"{num}-odd " for num in numbers]
# print(list1)

# Replace numbers greater than 10 with "Big"; otherwise "Small".
numbers = [12, 5, 18, 2, 25]
list2 = [f"{num}-Big" if num > 10 else f"{num}-Small" for num in numbers]
# print(list2)

# Return "Pass" if the mark is at least 50, otherwise "Fail".
marks = [95, 42, 77, 33, 88]
list3 = [f"{mark}-PASS" if mark >= 50 else f"{mark}-FAIL" for mark in marks]
print(list3)
