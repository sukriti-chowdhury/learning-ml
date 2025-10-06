"""
Given the following NumPy code, predict the output of the code:
"""
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = A[1:3, 0:2]

print(B)
B[0, 0] = 100
print(A)