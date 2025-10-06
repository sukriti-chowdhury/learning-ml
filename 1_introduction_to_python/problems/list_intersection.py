import json

def get_intersection(numbers1, numbers2):
    """
    Args:
     numbers1(list_int32)
     numbers2(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    intersection = []
    if len(numbers1) < len(numbers2):
        smaller_list = numbers1
        bigger_list = numbers2
    else:
        smaller_list = numbers2
        bigger_list = numbers1
        
    # Keep the bigger list in a dict with count, even though the count is not needed
    bigger_dict = dict()
    for n in bigger_list:
        if n in bigger_dict.keys():
            bigger_dict[n] += 1
        else:
            bigger_dict[n] = 1
    
    # print(bigger_dict)
    for n in smaller_list:
        if n in bigger_dict.keys() and n not in intersection:
            intersection.append(n)
    return intersection if len(intersection) > 0 else [-1]


# Read the sample_numbers.json file
with open('./introduction_to_python_1/resources/sample_numbers.json', 'r') as file:
    data = json.load(file)

# Extract the numbers from the JSON data
numbers1 = data.get('numbers1', [])
numbers2 = data.get('numbers2', [])

# PPrint the length of numbers1 and numbers2
#print("Length of numbers1:", len(numbers1))
#print("Length of numbers2:", len(numbers2))

print(get_intersection(numbers1, numbers2))
