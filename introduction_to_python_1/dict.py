"""
To demonstarte the use of dictionaries in Python, we can use the following code.
"""
# Characteristics of dictionaries:
# 1. Unordered collection of key-value pairs.
# 2. Keys must be unique and immutable. No duplicate keys allowed.
# 3. If a key is repeated, the last value will overwrite the previous one.
# 4. Values can be of any data type.

# Define a dictionary with string keys and integer values
dict_numbers: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

for key in dict_numbers.keys():
    print(f"Key: {key}")

for value in dict_numbers.values():
    print(f"Value: {value}")

for key, value in dict_numbers.items():
    print(f"Key: {key}, Value: {value}")

# Same as iterating over keys and accessing values
print("Iterating over keys and accessing values:")
for key in dict_numbers:
    print(f"Key: {key}, Value: {dict_numbers[key]}")