# import csv

# with open("students.csv") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)

# # Print the total number of students (excluding the header).
# with open("students.csv") as f:
#     reader = csv.reader(f)
#     next(reader)
#     row_count = 0
#     for row in reader:
#         row_count += 1
#         # print(row)
#     print(row_count)

# # Print the student with the highest marks.
# highest_mark = -1
# top_student = None

# with open("students.csv") as f:
#     reader = csv.reader(f)
#     next(reader)

#     for row in reader:
#         marks = int(row[2])

#         if marks > highest_mark:
#             highest_mark = marks
#             top_student = row

# print(f"Top Student:{row[0]} | Mark:{highest_mark}")


# # Calculate the average marks.
# students_count = 0
# total_marks = 0

# with open("students.csv") as f:
#     reader = csv.reader(f)
#     next(reader)

#     for row in reader:
#         students_count += 1
#         total_marks = total_marks + int(row[2])

# Average = round(total_marks / students_count, 2)
# print(f"Average Mark is {Average}")
