import numpy as np

A = np.random.randint(0, 10, size=(3, 3))

B = np.random.randint(0, 10, size=(3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

C = A + B
print("Matrix Addition:\n", C)

D = A - B
print("Matrix Subtraction:\n", D)

# Element-wise Multiplication
E = A * B
print("Element-wise Multiplication:\n", E)

# Matrix Multiplication (Dot Product)
F = np.dot(A, B)
print("Matrix Multiplication (Dot Product):\n", F)

# Matrix Transpose
G = np.transpose(A)
print("Matrix Transpose:\n", G)

# Matrix Inverse
H = np.linalg.inv(A)
print("Matrix Inverse:\n", np.round(H))

# Determinant
det_A = round(np.linalg.det(A))
print("Determinant of Matrix A:\n", det_A)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of Matrix A:\n", eigenvalues)
print("Eigenvectors of Matrix A:\n", eigenvectors)

# Accessing an element
element = A[0, 1]
print("Element at position (0, 1):\n", element)

