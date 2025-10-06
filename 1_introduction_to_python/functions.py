"""
To define a few different types of functions in Python, we can use the following code.
"""
# Define a function that uses a default argument
def greet(name: str = "John Doe", msg: str = "is welcome to the world of Python") -> str:
    """
    This function greets a person with a default message.
    
    :param name: The name of the person to greet. Defaults to "John Doe".
    :param msg: The message to include in the greeting. Defaults to "is welcome".
    :return: A greeting string.
    """
    return f"{name} {msg}"

print(greet())  # Using default arguments
print(greet("Alice"))  # Using a custom name
print(greet("Bob", "is learning Python"))  # Using custom name and message

# Define a function that returns a tuple
def get_results(a: int, b: int) -> tuple:
    """
    This function returns a tuple containing two integers.
    
    :return: A tuple with two integers.
    """
    return a + b, a - b

# Call the function and unpack the tuple
result_sum, result_diff = get_results(10, 5)
print("Sum:", result_sum)  # Output: Sum: 15
print("Difference:", result_diff)  # Output: Difference: 5

# Define a lambda function that squares a number
square = lambda x: x ** 2
# Call the lambda function
print("Square of 5:", square(5))  # Output: Square of 5

# A multiline lambda function (not recommended for readability)
multiline_lambda = lambda x: (
    x ** 2,
    x ** 3,
    x ** 4
)
# Call the multiline lambda function
print("Multiline lambda results for 2:", multiline_lambda(2))  # Output: Multiline lambda results for 2: (4, 8, 16)