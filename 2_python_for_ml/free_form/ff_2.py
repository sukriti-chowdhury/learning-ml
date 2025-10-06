"""
Using NumPy, create a 5x5 identity matrix and add a scalar value of 5 to it.
Multiply the resulting matrix with a 5x1 column vector filled with random integers between 1 and 10.
Print the resulting vector.
"""

import numpy as np

# Create a 5x5 identity matrix
# An identity matix fills all the diagonal elements with 1 and all other elements with 0
def create_identity_matrix(size: int) -> np.ndarray:
    return np.eye(size, dtype=int)

identity_matrix: np.ndarray = create_identity_matrix(5)
print('identity_matrix:')
print(identity_matrix)

identity_matrix = identity_matrix + 5
print('identity_matrix with a scalar value 5:')
print(identity_matrix)

# Create a 5x1 column vector filled with random integers between 1 and 10
vector: np.ndarray = np.random.randint(1, 10, 5).reshape(5, 1)

print('5x1 column vector:')
print(vector)

# Now multiply the resulting matrix with the column vector
resulting_vector: np.ndarray = identity_matrix * vector
print('Resulting vector after multiplication:')
print(resulting_vector)
