"""
Write a Python program that uses global and local variables to perform a calculation.
Print the values of both the global and local variables before and after the calculation.
"""

# To calculate the area of a circle, we use A = PI * r**2, where PI = 3.14 and r = radius of the circle.

import random
pi: float = 0 # Not initializing here, will initialize inside the function

# Following function calculates the area of the circle and then adds a random float value to the 
def inflated_area_of_circle(radius: float) -> float:
    global pi
    pi = 3.14
    area_inflation: float = random.choices(range(1, 5), k=1)
    print(area_inflation)
    inflated_area: float = (pi * radius**2) + area_inflation[0]
    print(inflated_area)
    return inflated_area

print(pi)
area: float = inflated_area_of_circle(4)
print(pi)
print(area)

