"""
To perform any quick test of a specific understanding of Python.
"""
number = 5261
sum = 0
for digit in str(number):
    sum += int(digit)
    
print(sum)

a: str = "Hello, World!"

def adding(x: int, y: int) -> int:
    """Returns the sum of x and y."""
    print(type(x), type(y))  # Check types of x and y
    return x + y

print(adding(a, "Johny"))

integers: list[int] = [1, 2, 3, 4, 5]
print(integers.insert(2, 10))  # Insert 10 at index 2, and moves subsequent elements
print(integers)  # Output: [1, 2, 10, 3, 4, 5]
integers[1] = "Hello" # This replaces a value at the index 1
# Can be heterogeneous
print(integers)

# sentence = input()
# print("Length of the input sentence is:", len(sentence))

greeting: str = "Hello, World!"
print(greeting[-1::-1])  # Reverse the string using slicing

str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub, 4))

for i in range(0, 0):
    print("Hello World!!!")  # Print numbers from 0 to 9 in one line

print("Outer hello world!!!")
