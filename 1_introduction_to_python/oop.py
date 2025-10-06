"""
To demonstrate diffrent aspects of Object-Oriented Programming (OOP) in Python, we can use the following code.
# OOP is a programming paradigm that uses objects and classes to structure code.
"""

# Define a class named `Animal`, add a class variable, an instance variable, and a method.
class Animal:
    # Class variable
    species: str = "Generic Animal"

    # Constructor to initialize instance variables
    def __init__(self, name: str, age: int):
        # Instance variables
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic sound"
    
# Encapsulation: Define a class `Dog` that inherits from `Animal` and overrides the `make_sound` method.
# Encapsulation is the bundling of relevant data and methods that operate on that data within one unit, or class.
class Dog(Animal):
    # Class variable
    species: str = "Dog"

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.breed = breed  # Instance variable specific to Dog

    def make_sound(self):
        return "Woof Woof"
    
# Abstraction: Define a class `Bird` that inherits from `Animal` and overrides the `make_sound` method.
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.
class Bird(Animal): 
    # Class variable
    species: str = "Bird"

    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.wing_span = wing_span  # Instance variable specific to Bird

    def make_sound(self):
        return "Chirp Chirp"
    
#Inheritance: Define a class `Fish` that inherits from `Animal` and overrides the `make_sound` method.
# Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.
class Fish(Animal):
    # Class variable
    species: str = "Fish"

    def __init__(self, name: str, age: int, fin_size: float):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.fin_size = fin_size  # Instance variable specific to Fish

    def make_sound(self):
        return "Blub Blub"

# Polymorphism: Define a class `Cat` that also inherits from `Animal` and overrides the `make_sound` method.
# Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.
class Cat(Animal):
    # Class variable
    species: str = "Cat"

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.color = color  # Instance variable specific to Cat

    def make_sound(self):
        return "Meow Meow"
    
# Static polymorphism: Method resolution at compile time, typically through method overloading.
# Python does not support method overloading like some other languages, but we can achieve similar behavior
# Note: In Python, the last defined function will override the previous ones, so this is not true method overloading.
def add(a: int, b: int) -> int:
    return a + b
def add(a: int, b: int, c: int) -> int:
    return a + b + c

print(add(5, 10, 15))  # Output: 30
# print(add(5, 10))  # Uncommenting this will raise TypeError: add() missing 1 required positional argument: 'c'

# Dynamic polymorphism: Method resolution at runtime, typically through method overriding.
# Create instances of each class
dog = Dog("Buddy", 3, "Golden Retriever")
bird = Bird("Tweety", 2, 0.25)
cat = Cat("Whiskers", 4, "Tabby")
fish = Fish("Nemo", 1, 0.1)

print(f"{dog.name} is a {dog.species} and makes sound: {dog.make_sound()}")
print(f"{bird.name} is a {bird.species} and makes sound: {bird.make_sound()}")
print(f"{cat.name} is a {cat.species} and makes sound: {cat.make_sound()}")
print(f"{fish.name} is a {fish.species} and makes sound: {fish.make_sound()}")