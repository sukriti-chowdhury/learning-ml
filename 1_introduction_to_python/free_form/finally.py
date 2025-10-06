"""
How can you ensure that a certain code block runs no matter whether there’s an exception or not?
Ans: By using finally block with try
"""
import traceback

def division(a: int, b: int) -> float:
    try:
        return a / b
    except Exception as e:
        print(f"First, let's print the error message only. Error - {e}")
        print('Now printing traceback below - ')
        traceback.print_exc()
    finally:
        print('This block will br printed irrespective of the raised exception')

print(division(13, 7))
print(division(12, 4))
print(division(18, 0))