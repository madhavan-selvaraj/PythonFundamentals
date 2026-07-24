# with open ('student_db.txt','w') as f:
#     f.writelines(
#         "John,85\n"
#         "Alice,92\n"
#         "Bob,78\n"
#         "David,88\n"
#     )


highest_mark = 0
topper_name = ""
students_count = 0
total_mark = 0
count_above_80 = 0
students = {}
with open("student_db.txt") as f:
    for line in f:
        name, mark = line.strip().split(",")
        mark = int(mark)
        students_count += 1
        total_mark += mark
        students[name] = mark

        # Find topper.
        if mark > highest_mark:
            highest_mark = mark
            topper_name = name

        # Count students scoring above 80.
        if mark > 80:
            count_above_80 += 1


average_mark = total_mark / students_count

print(f"Topper name:{topper_name},Highest mark:{highest_mark}")
print(f"Average Marks is {average_mark}")
print(f"Count of Students Scoring above 80 is {count_above_80}")

# Sort by marks (descending)
sort_by_mark = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))

# Save the sorted data to a new file.

with open("sorted_marks.txt", "w") as f:
    for name, mark in sort_by_mark.items():
        f.write(f"{name},{mark}\n")
    print("Sorted Students name and marks added to sorted_marks.txt successfully")
