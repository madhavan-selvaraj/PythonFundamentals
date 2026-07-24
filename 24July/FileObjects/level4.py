# Write a program that counts the number of lines in a file.
# line_count=0
# with open('student.txt') as f:
#     for line in f:
#         print(line,end='')
#         line_count+=1
# print(f"Number of lines:{line_count}")

# Count the total number of words.

# with open('student.txt') as f:
#     context=f.read()
# mylist=context.split()
# print(len(mylist))

# Count the total number of characters.

# with open('student.txt') as f:
#     context=f.read()
# # total_char=0
# # for i in context:
# #     total_char+=1
# # print(total_char)
# print(len(context))

# Find how many vowels are present in the file.
# with open('student.txt') as f:
#     content=f.read().lower()
# vowels=('a','e','i','o','u')
# count=0

# for char in content:
#     if char in vowels:
#         count+=1
# print(count)

# Print the longest and Shortest line in the file.
# longest_line=""

# shortest_line=None
# with open('student.txt') as f:

#     for line in f:
#        if len(line)>len(longest_line):
#            longest_line=line

#        if shortest_line is None or len(line)<len(shortest_line):
#            shortest_line=line

# print(f"Longest Line:{longest_line}\n"
#       f"Line Count:{len(longest_line)}"
#     )

# print(f"Shortest Line:{shortest_line}\n"
#       f"Line Count:{len(shortest_line)}"
#     )

# Print the file contents in reverse order (last line first).

# with open('student.txt') as f:
#     content=f.readlines()

# for line in reversed(content):
#     print(line,end="\n")

# Read one file and create another file where every character is uppercase.

# with open('student.txt') as f:
#     content=f.read()

# with open('upper_student.txt','w') as f:
#     f.write(content.upper())

