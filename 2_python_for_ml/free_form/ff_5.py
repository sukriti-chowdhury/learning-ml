"""
Write a Python program using NumPy to create a 10x10 matrix filled with random integers between 1 and 100.
Find the minimum and maximum values of the matrix along with their indices.
"""

import numpy as np

matrix: np.ndarray = np.random.randint(1, 101, (10, 10))
min_val = np.min(matrix)
max_val = np.max(matrix)
print("argmin:", np.argmin(matrix))
min_idx = np.unravel_index(np.argmin(matrix), matrix.shape)
max_idx = np.unravel_index(np.argmax(matrix), matrix.shape)
print("Matrix:\n", matrix)
print("Minimum value:", min_val, "at index:", min_idx)
print("Maximum value:", max_val, "at index:", max_idx)