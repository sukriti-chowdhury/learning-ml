"""
Write a Python program using NumPy to create a 1D array of 20 elements with random integers between 1 and 100.
Calculate the number of even and odd elements in the array and print the result.
"""

import numpy as np

array_1: np.ndarray = np.random.randint(1, 100, 20)
print('array_1:')
print(array_1)
print(f"Number of evens: {array_1[array_1 % 2 == 0].size}")
print(f"Number of odds: {array_1[array_1 % 2 != 0].size}")