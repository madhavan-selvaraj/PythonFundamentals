# import csv

# with open('studentss.csv','w') as f:
#     writter=csv.writer(f)
#     writter.writerow(["ID","Name","Marks"])
#     writter.writerow(["1","Alice","85"])
#     writter.writerow(["2","Bob","90"])
#     writter.writerow(["3","Charlie","88"])


# students = [
#     [1,"Alice",85],
#     [2,"Bob",90],
#     [3,"Charlie",88]
# ]

# with open('studentss.csv','w') as f:
#     writter=csv.writer(f)
#     writter.writerow(["ID","Name","Marks"])
#     writter.writerows(students)


# students = [
#     {"ID":1,"Name":"Alice","Marks":85},
#     {"ID":2,"Name":"Bob","Marks":90},
#     {"ID":3,"Name":"Charlie","Marks":88}
# ]

# with open('studentss.csv','w',newline="") as f:
#     fieldnames=["ID","Name","Marks"]

#     writter=csv.DictWriter(f,fieldnames=fieldnames)
#     writter.writeheader()
#     writter.writerows(students)


# new_student=[4,"David",92]

# with open('studentss.csv','a',newline="") as f:
#     writter=csv.writer(f)
#     writter.writerow(new_student)
