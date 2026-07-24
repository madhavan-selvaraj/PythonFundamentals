# import json

# Add a New Student
# new_student={
#             "id":4,
#             "name":"John",
#             "marks":89
#         }

# with open("students.json") as f:
#     students=json.load(f)

# students.append(new_student)

# with open("students.json","w") as f:
#     json.dump(students,f,indent=4)


# Update Marks
# with open("students.json") as f:
#     students=json.load(f)

# for data in students:
#     if data['name']=="Alice":
#         data['marks']=96

# with open("students.json","w") as f:
#     json.dump(students,f,indent=4)

# Delete Bob from the JSON file.

# with open("students.json") as f:
#     students=json.load(f)

# for data in students:
#     if data['name']=="Bob":
#         students.remove(data)

# with open("students.json","w") as f:
#     json.dump(students,f,indent=4)

# Search Student
# student_name=input("Enter student name to search:")

# with open("students.json") as f:
#           students=json.load(f)
# for data in students:
#     if data['name']==student_name:
#         print(f"Student found: {data['name']}, Marks: {data['marks']}")

# with open("students.json") as f:
#     students=json.load(f)

# sort_student=sorted(students,key=lambda x:x['marks'],reverse=True)

# with open("sorted_students.json","w") as f:
#     json.dump(sort_student,f,indent=4)
