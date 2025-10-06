"""
Using NumPy, create a 1000-element array of random integers between 1 and 1000.
Calculate the cumulative sum of the array and print the 10th, 100th, and 500th elements of the cumulative sum array.
"""

import numpy as np

array_1: np.ndarray = np.random.randint(1, 1000, 1000)

cumulative_sum: np.ndarray = np.cumsum(array_1)

print(cumulative_sum[9])
print(cumulative_sum[99])
print(cumulative_sum[499])