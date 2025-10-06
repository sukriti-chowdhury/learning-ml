"""
Reverse the words in a given string.
"""

def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    return " ".join(reversed(s.split()))

# Example usage
sample_string = "Hello World from Python"
reversed_string = reverse_words(sample_string)
print(reversed_string)
