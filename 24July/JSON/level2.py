# import json

# Write Multiple Students
# students = [
#     {"id":1,"name":"Alice","marks":91},
#     {"id":2,"name":"Bob","marks":85},
#     {"id":3,"name":"David","marks":95}
# ]

# with open("students.json","w") as f:
#     json.dump(students,f,indent=4)

# Read All Students
# with open ("students.json") as f:
#     students=json.load(f)

# for data in students:
#     print(f"{data['name']}-{data['marks']}")

# # Find Highest Marks,Average Marks,Count Students.
# highest_mark=0
# student_count=0
# total_mark=0

# with open("students.json") as f:
#     students=json.load(f)

# for data in students:
#     student_count+=1
#     total_mark+=data['marks']
#     if int(data['marks'])>highest_mark:
#         highest_mark=int(data['marks'])

# average=round(total_mark/student_count,2)
# print(f"Highest Mark:{highest_mark}")
# print(f"Average Mark:{average}")
# print(f"Total Students:{student_count}")
