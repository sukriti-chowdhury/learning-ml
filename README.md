# Learning ML: Introduction to Python

This repository contains introductory Python scripts designed to help beginners understand the basics of Python programming, with a focus on operators and simple input/output. The code examples are suitable for those new to programming or Python, and are intended as a foundation for further exploration in machine learning and data science.

## Folder Structure

```
learning-ml/
│
├── introduction_to_python_1/
│   ├── hello_world.py
│   └── operators.py
└── README.md
```

## File Descriptions

### `introduction_to_python_1/hello_world.py`
A simple script that prints "Hello, World!" to the console. This is typically the first program written when learning a new programming language.

### `introduction_to_python_1/operators.py`
This script demonstrates the use of various operators in Python, including:
- **Arithmetic Operators**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), Floor Division (`//`), Modulus (`%`), Exponentiation (`**`), and Bitwise Left Shift (`<<`).
- **Identity Operators**: `is`, `is not` (checks if two variables point to the same object in memory).
- **Equality Operator**: `==` (checks if the values are equal).
- **Membership Operator**: `in` (checks if a value exists within a sequence).
- **Input/Output**: Demonstrates how to take user input and print output.

#### Example Output
```
a + b = 13
a - b = 7
a * b = 30
a / b = 3.3333333333333335
a // b = 3
a % b = 1
a ** b = 1000
a << b = 80
'H' in str = True
a is b = False
a is c = True
x == y = True
x is y = False
a == c = True
a is not b = True
a is d = True
Enter your name: John
Enter your age: 25
Hello, John
You are 25 years old.
```

## Getting Started

1. **Clone the repository:**
   ```powershell
   git clone <repository-url>
   cd learning-ml
   ```
2. **Navigate to the scripts:**
   ```powershell
   cd introduction_to_python_1
   ```
3. **Run a script:**
   ```powershell
   python hello_world.py
   python operators.py
   ```

## Requirements
- Python 3.x

No external libraries are required for these scripts.

## License
This project is for educational purposes.