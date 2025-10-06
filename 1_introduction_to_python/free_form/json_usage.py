"""
Write a Python program that reads data from a JSON file and prints the contents of the file to the console.
"""

import json

def read_json(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        data: str = json.load(file)
        return data

footballers: str = read_json('./introduction_to_python_1/resources/footballers.json')    
print(footballers)
print("Now let's print it pretty")
print(json.dumps(footballers, indent=4))