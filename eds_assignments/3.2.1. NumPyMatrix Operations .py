import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
add_res = matrix_a + matrix_b
print("Addition (A + B):")
print(add_res)
# Subtraction
sub_res = matrix_a - matrix_b
print("Subtraction (A - B):")
print(sub_res)
# Multiplication (element-wise)
mul_res = matrix_a * matrix_b
print("Element-wise Multiplication (A * B):")
print(mul_res)
# Matrix multiplication (dot product)
dot_res = np.dot(matrix_a, matrix_b)
print("A dot B:")
print(dot_res)
# Transpose
trans_res = matrix_a.T
print("Transpose of A:")
print(trans_res)