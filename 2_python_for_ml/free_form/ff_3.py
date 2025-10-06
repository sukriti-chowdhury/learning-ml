"""
Write a Python program using NumPy to create two 3x3 matrices filled with random integers between 1 and 100.
Compute their element-wise multiplication, and print the resulting matrix.
"""

import numpy as np

array_1: np.ndarray = np.random.randint(1, 10, 9).reshape(3, 3)
array_2: np.ndarray = np.random.randint(1, 10, 9).reshape(3, 3)

print('Array 1:')
print(array_1)
print('Array 2:')
print(array_2)

print('Element-wise multiplication:')
print(array_1 * array_2)
print(np.multiply(array_1, array_2))