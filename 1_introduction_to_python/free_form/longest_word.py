"""
 Write a Python program to find the longest word in a file.
"""

# Solution 1 : Using built in max function

def longest_word(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        words = f.read().split()
        return max(words, key=len) if words else ''
    
print(longest_word('./introduction_to_python_1/resources/ai_story.txt'))


# Solution 2 : By calculating the length of each word
import traceback
def longest_word_custom(file_path: str) -> str:
    longest_word: str = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                words: list[str] = line.split()
                for word in words:
                    if len(word) > len(longest_word):
                        longest_word = word
        return longest_word
    except:
        traceback.print_exc()

print(longest_word('./introduction_to_python_1/resources/ai_story.txt'))