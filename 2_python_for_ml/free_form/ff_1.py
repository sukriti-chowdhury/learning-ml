"""
Write a Python program using NumPy to create a 5x5 matrix filled with random integers between 1 and 100.
Calculate the mean and standard deviation of the matrix and print them.
"""

import numpy as np

def mean_and_stddiv() -> tuple[int, int]:

    # Create a 5 X 5 matrix filled with random integers from 1 and 100
    array_1 = np.random.randint(1, 100, 25).reshape(5, 5)
    print('Original Array:')
    print(array_1)
    return (np.mean(array_1), np.std(array_1))

# Call the function
print(f"Mean = {mean_and_stddiv()[0]:.2f}, Standard Deviation = {mean_and_stddiv()[1]:.2f}")

