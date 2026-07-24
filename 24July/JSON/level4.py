# # import json


# # students = [
# #     {
# #         "id":1,
# #         "name":"Alice",
# #         "subjects":{
# #             "Math":95,
# #             "Science":88,
# #             "English":91
# #         }
# #     },
# #     {
# #         "id":2,
# #         "name":"Bob",
# #         "subjects":{
# #             "Math":80,
# #             "Science":75,
# #             "English":85
# #         }
# #     }
# # ]

# # with open("students.json","w") as f:
# #     json.dump(students,f,indent=4)


# with open("students.json") as f:
#     students = json.load(f)

# for data in students:
#     print(f"{data['name']}\n")
#     print("Subject\n")
#     for subject, marks in data["subjects"].items():
#         print(f"{subject}:{marks}")
