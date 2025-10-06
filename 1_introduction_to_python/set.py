"""
To demonstrate the use of sets in Python, we can use the following code.
"""
# Characteristics of sets:
# 1. Unordered and unique elements. No duplicate elements allowed.
# 2. Mutable, but elements must be immutable.
# 3. Can add or remove elements.

# Define sets of Strings
fruits_1: set[str] = {"apple", "banana", "cherry"}
fruits_2: set[str] = {"fig", "banana", "grape"}

print("Union of two sets:", fruits_1 | fruits_2)  # Union
print("Another way to get union:", fruits_1.union(fruits_2))  # Union using method
print("Intersection of two sets:", fruits_1 & fruits_2)  # Intersection
print("Another way to get intersection:", fruits_1.intersection(fruits_2))  # Intersection using method
print("Difference of two sets:", fruits_1 - fruits_2)  # Difference
print("Another way to get difference:", fruits_1.difference(fruits_2))
print("Symmetric difference of two sets:", fruits_1 ^ fruits_2)  # Symmetric difference
print("Another way to get symmetric difference:", fruits_1.symmetric_difference(fruits_2))