"""
This module demonstrates the use of various NumPy attributes.
"""
import numpy as np

def create_3d_array() -> np.ndarray:
    """Creates and returns a 3D NumPy array of integers 1 to 12."""
    return np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

def print_array_attributes(array_3d: np.ndarray) -> None:
    """Prints the array and its attributes."""
    print("3D Array:")
    print(array_3d)
    # Get the integer 9
    print(array_3d[1][0][2])
    # Print attributes
    print(f"Array 1, NDim = {array_3d.ndim}")
    print(f"Array 1, Shape = {array_3d.shape}")
    print(f"Array 1, Size = {array_3d.size}")
    print(f"Array 1, Dtype = {array_3d.dtype}")

if __name__ == "__main__":
    arr: np.ndarray = create_3d_array()
    print_array_attributes(arr)