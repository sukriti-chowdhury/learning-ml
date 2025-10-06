"""
To demonstrate the use of lambda functions in Python.
Lambda functions are small anonymous functions defined using the `lambda` keyword.
They can take any number of arguments but can only have one expression.
Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
Lambda functions are very helpful to write concise code, especially when used with functions like `map()`, `filter()`, `reduce()` and `sorted()`.
"""

# A list of integers
numbers: list[int] = [1, 2, 3, 4, 5]

# Using a lambda function to square each number in the list
squared_numbers: list[int] = list(map(lambda x: x ** 2, numbers))
print (squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using a lambda function to filter even numbers from the list
even_numbers: list[int] = list(filter(lambda x: x % 2 == 0, numbers))
print (even_numbers)  # Output: [2, 4]

# Using reduce to compute the product of the numbers
from functools import reduce
product_of_numbers: int = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120
