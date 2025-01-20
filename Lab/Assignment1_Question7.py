import random

def generate_matrix(rows, cols, lower, upper):
    return [[random.uniform(lower, upper) for _ in range(cols)] for _ in range(rows)]

def count_sign_changes(matrix):
    sign_changes = 0
    for row in matrix:
        for i in range(1, len(row)):
            if (row[i] >= 0 > row[i-1]) or (row[i] < 0 <= row[i-1]):
                sign_changes += 1
    return sign_changes

rows, cols = 6, 5
matrix = generate_matrix(rows, cols, -1, 1)

print("Matrix A:")
for row in matrix:
    print(row)

sign_changes = count_sign_changes(matrix)
print(f"\nNumber of sign changes in the matrix: {sign_changes}")
