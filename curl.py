import numpy as np

# Define a matrix
matrix = np.array([[-0.32, -0.94], [-0.94, 0.32]])

# Compute the eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Create a list of tuples containing the eigenvectors and eigenvalues
eigenpairs = list(zip(eigenvectors, eigenvalues))

# Sort the list by the eigenvalues
eigenpairs.sort(key=lambda x: x[1])

# Print the sorted list of eigenpairs
print(eigenpairs)
