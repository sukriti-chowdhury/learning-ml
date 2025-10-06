"""
To perform any quick test of a specific understanding of Python.
"""
persons = [('Alice', 30, 'Orange County'), ('Bob', 25, 'Los Angeles'), ('Charlie', 35, 'New York')]

names = [person[0] for person in persons]
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

cities = [city for name, age, city in persons]
print(cities)  # Output: ['Orange County', 'Los Angeles', 'New York']

my_lambda = lambda x: (
    x * 2
    if x > 10
    else x + 2
)

print(my_lambda(5))   # Output: 7
print(my_lambda(15))  # Output: 30

numbers = [1, 2, -9, 3, 4, 0, -1, 5]
negative_numbers = list(filter(lambda x: x < 0, numbers))
print(negative_numbers)  # Output: [-9, -1]

even_numbers = list(filter(lambda x: x %2 == 0 and x > 0, numbers))
print(even_numbers)

# Bitwise XOR operation on boolean values
print("Bitwise XOR operation results:")
print(True ^ True)
print(False ^ False)
print(True ^ False)
print(False ^ True)

# Bitwise OR operation on boolean values
print("Bitwise OR operation results:")
print(True | True)
print(False | False)
print(True | False)
print(False | True)