"""
To define a few different types of functions in Python, we can use the following code.
"""
# Built in function type
print(type(100))  # Output: <class 'int'>
print(type(100.0))  # Output: <class 'float'>
print(type("Hello World!"))  # Output: <class 'str'>

words: list[str] = ["Hello", "World", "Python"]
print(type(words))  # Output: <class 'list'>

tuple_int = (1, 2, 3)
print(type(tuple_int))  # Output: <class 'tuple'>

class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def print_car(self):
        print(f"Car Make: {self.make}, Model: {self.model}")

car = Car("Toyota", "Corolla")
car.print_car()
print(type(car))