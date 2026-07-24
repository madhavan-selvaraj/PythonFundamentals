# 6. Append Data
# Append the following line to the file.
# "College: ABC University"

# with open('student.txt','a') as f:
#     f.write("College : ABC University \n")

# 7. Overwrite File
# Open the file in write mode and replace everything with
# "Python Programming"

# with open ('student.txt','w') as f:
#     f.write("Python Programming\n")

# 8. Exclusive Creation
# Create a file named report.txt
# using the mode that raises an error if the file already exists.
# Handle the exception.

# try:
#     with open('report.txt','a') as f:
#         f.write("Report Created Successfully\n")
# except FileExistsError:
#     print("report.txt already exists")

# 9. Binary Mode
# Write bytes into a binary file named data.bin.
# Example:
# b"Hello Python"
# Read them back.

# with open('data.bin','wb') as f:
#     f.write(b"Hello Python")

# with open('data.bin','rb') as f:
#     print(f.read())
