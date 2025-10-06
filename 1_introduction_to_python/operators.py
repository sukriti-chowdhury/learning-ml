"""
To test out how some of the operators work in Python, we can use the following code.
This code demonstrates the use of various operators in Python.
"""

# Define integer variables
a:int = 10
b:int = 3
c:int = 10
d:int = a

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# Print the values of a and b
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a << b =", a << b)  # Left Shift

# Other operators, in and is
str = "Hello, World!"
print("'H' in str =", 'H' in str)  # Membership
print("a is b =", a is b)  # Identity, it checks if both variables point to the same object. == checks for value equality
print("a is c =", a is c)  # Identity, true because internally is the same object
print("x == y =", x == y)  # Equality, checks if the values are the same
print("x is y =", x is y)  # Identity, false because they are different
print("a == c =", a == c)
print("a is not b =", a is not b)  # Identity
print("a is d =", a is d)  # Identity

# input function
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name)
print("You are", age, "years old.")