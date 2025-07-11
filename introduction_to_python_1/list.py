"""
To demonstrate the use of lists in Python, we can use the following code.
"""

# Define a list of integers
numbers: list[int] = [1, 2, 3, 4, 5]
strings: list[str] = ["apple", "banana", "cherry"]

# Concatenate two lists
combined_list: list = numbers + strings
# Print the combined list
print("Combined List:", combined_list)
print(type(combined_list)) 
print(type(numbers))

# Repeat a list
repeated_list: list[int] = numbers * 2
# Print the repeated list
print("Repeated List:", repeated_list)

# Negative indexing
print("Last element of numbers:", numbers[-1])  # Output: 5
print("Second last element of strings:", strings[-2])  # Output: banana

# List slicing
print("First 3 numbers in the list:", numbers[:3])
print("Last 2 numbers in the list:", numbers[-2:])
print("Alternate elements in numbers:", numbers[::2])  # Output: [1, 3, 5]
print("Reverse of numbers:", numbers[::-1])  # Output: [5, 4, 3, 2, 1]

# Difference between list and tuple, tuple is immutable
tuple_numbers: tuple[int, ...] = (1, 2, 3, 4, 5)
print("Tuple of numbers:", tuple_numbers)
# Attempting to modify a tuple will raise an error
# tuple_numbers[0] = 10  # Uncommenting this line will raise a TypeError

# Write down all the differences between list and tuple
# 1. Lists are mutable, tuples are immutable.
# 2. Lists are defined using square brackets [], while tuples are defined using parentheses ().
# 3. Lists have more built-in methods compared to tuples.
# 4. Tuples can be used as keys in dictionaries, while lists cannot.
# 5. Lists can grow and shrink in size, while tuples have a fixed size.
# 6. Lists are generally slower than tuples due to their mutability. IMPORTANT

# Sorting a list of tuples
tuples_list: list[tuple[int, str]] = [(3, "three"), (1, "one"), (1, "ek"), (2, "two")]
print(sorted(tuples_list))  # Sorts by the first element of each tuple