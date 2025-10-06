"""
Write a Python program using NumPy to create a 2D array of size 8x8, 
where the outer border elements are set to 1 and the inner elements are set to 0.
Print the resulting array.
"""

import numpy as np

array_1: np.ndarray = np.ones((8, 8), dtype=int)
array_1[1:-1, 1:-1] = 0
print(array_1)