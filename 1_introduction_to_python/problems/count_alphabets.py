"""
To count alphabets in a given string
"""
# Solution#1
def count_alphabets(s: str) -> int:
    """
    Args:
     s(str)
    Returns:
     int
    """
    return sum(c.isalpha() for c in s)

# Solution#2
def count_alphabets_2(s: str) -> int:
    """
    Args:
     s(str)
    Returns:
     int
    """
    alphabets: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count: int = 0
    for c in s:
        if c.lower() in alphabets:
            count += 1
    return count

# Example usage
sample_string = "Hello World 123!"
print(count_alphabets_2(sample_string))