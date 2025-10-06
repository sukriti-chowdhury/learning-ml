"""
Write a Python program using NumPy to create a 5x5 matrix filled with random floats between 0 and 1.
Replace the maximum value in the matrix with 0 and print the original and modified matrices.
"""

import numpy as np

numbers: np.ndarray = np.random.uniform(0, 1, 25).reshape(5, 5)
print('Original Array:')
print(numbers)

max_value: np.float64 = np.max(numbers)
print(max_value)
max_index = np.unravel_index(np.argmax(numbers), numbers.shape)
print('Max value index:', max_index)

# Solution 1
numbers[numbers == max_value] = 0
print('Modified Array:')
print(numbers)

# Solution 2
numbers[max_index] = 0
print('Modified Array with max value replaced by 0:')
print(numbers)