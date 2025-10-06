import numpy as np

print("Running test.py")

x: np.ndarray = np.array([[1, 2, 3], [4, 5, 6]])
y: np.ndarray = np.array([[7, 8, 9], [10, 11, 12]])
z: np.ndarray = np.concatenate((x, y), axis=1)

print("Array z:")
print(z)

print(np.sum(x))