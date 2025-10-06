"""
To practice numpy
"""

import numpy as np

# Transposing a 2D array
# Create a 2D array and transpose it
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.T

print(b)

# hstack and vstack
# Create two 2D arrays and stack them horizontally and vertically
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[7, 8, 9], [10, 11, 12]])
hstacked = np.hstack((c, d))
vstacked = np.vstack((c, d))

print("Horizontal Stack:")
print(hstacked)
print("Vertical Stack:")
print(vstacked)

array_1 = np.array([10, 20, 30, 40])
mask = (array_1 >= 20) & (array_1 <= 30)
print(type(mask))
print(mask)
array_2 = array_1[mask]
print(array_2)

x = np.array([
    [
        [1, 2],
        [3, 4]
    ], 
    [
        [5, 6], 
        [7, 8]
    ]
])
print(x.shape)

y = np.array([1, 2, 3, 4, 5])
print(y.shape)

print(np.diagonal(x))
print(np.trace(x))