"""
 Given the following NumPy code, predict the output of the code:
"""
import numpy as np

A = np.arange(1, 17).reshape(4, 4)
B = A[:, ::-1]
print('Original Array:')
print(A)
print('Modified Array:')
print(B)

"""
[
    [1,  2,  3,  4]
    [5,  6,  7,  8]
    [9,  10, 11, 12]
    [13, 14, 15, 16]
]

[
    [13, 14, 15, 16]
    [9,  10, 11, 12]
    [5,  6,  7,  8]
    [1,  2,  3,  4]
]

"""