import csv

# Print Only Names
# with open('employee.csv') as f:
#     reader=csv.reader(f)
#     next(reader)

#     for row in reader:
#         print(row[1])


# Print IT Employees
# with open('employee.csv') as f:
#     reader=csv.reader(f)
#     next(reader)

#     for row in reader:
#         if row[2] == "IT":
#             print(row[1])

# Find Highest Salary
# max_salary=0
# employee_name=None
# with open('employee.csv') as f:
#     reader = csv.reader(f)
#     next(reader)

#     for row in reader:
#         if int(row[3]) > max_salary:
#             max_salary=int(row[3])
#             employee_name=row[1]
# print(f"{employee_name}:{max_salary}")


# Count Employees Department-wise
# it_count=0
# hr_count=0
# finance_count=0
# with open("employee.csv") as f:
#     reader=csv.reader(f)
#     next(reader)

#     for row in reader:
#         if row[2] == "IT":
#             it_count+=1
#         elif row[2] == "HR":
#             hr_count+=1
#         elif row[2] == "Finance":
#             finance_count+=1
# print(f"IT:{it_count}")
# print(f"HR:{hr_count}")
# print(f"FINANCE:{finance_count}")


# Average Salary by Department

it_count = 0
it_salary = 0
hr_count = 0
hr_salary = 0
finance_count = 0
finance_salary = 0

with open("employee.csv") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        if row[2] == "IT":
            it_count += 1
            it_salary += int(row[3])
        elif row[2] == "HR":
            hr_count += 1
            hr_salary += int(row[3])
        elif row[2] == "Finance":
            finance_count += 1
            finance_salary += int(row[3])

it_average = it_salary / it_count
hr_average = hr_salary / hr_count
finance_average = finance_count / finance_count

print(f"IT:{it_average}")
print(f"HR:{hr_average}")
print(f"FINANCE:{finance_average}")
