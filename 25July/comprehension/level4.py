# Create a 3 × 3 matrix filled with zeros.
matrix = [[0 for i in range(3)] for j in range(3)]
# print(matrix)

# Create the following multiplication table:
# 1 2 3
# 2 4 6
# 3 6 9
# 4 8 12
table = [[i * j for i in range(1, 4)] for j in range(1, 5)]
for row in table:
    pass
    print(row, "\n")

# Flatten the following list:
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)
