"""
Write a Python program to sort a list of strings based on the length of each string.
Define a custom sort function that takes a list of strings and returns a sorted list.
"""
import math

# Solution 1 : Using built-in sort method

def custom_sort_bi(names: list[str]) -> list[str]:
    names.sort(key=lambda name: len(name))
    return names

students: list[str] = ['Alice', 'Bob', 'Zion', 'Aaron', 'Max', 'Jackey', 'Emily', 'Jackson']
print(sorted(students))
print(custom_sort_bi(students))


# Solution 2 : Using custom sort method, divide and conquer

# Merge utility function, this assumes both the left and right lists are sorted
def merge(left: list[str], right: list[str]) -> list[str]:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    l = r = 0
    merged: list[str] = []

    while l < len(left) and r < len(right):
        if len(left[l]) > len(right[r]):
            merged.append(right[r])
            r += 1
        else:
            merged.append(left[l])
            l += 1

    # Now add any remaining elements from the list
    while l < len(left):
        merged.append(left[l])
        l += 1

    while r < len(right):
        merged.append(right[r])
        r += 1

    return merged
    
def sort_by_length(names: list[str]) -> list[str]:

    if len(names) <= 1:
        return names
    
    midpoint: int = math.floor(len(names) / 2)
    left: list[str] = names[:midpoint]
    right: list[str] = names[midpoint:]

    left = sort_by_length(left)
    right = sort_by_length(right)
    
    return merge(left, right)

print(f"Print using custom built function - {sort_by_length(students)}")