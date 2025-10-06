""" To demonstrate the implementation of merge sort """
# As a first step, we define the merge function
# This assumes that the two input lists are already sorted
# This function returns the merged array in sorted order
def merge(left, right):
    result = []
    i = j = 0
    # If left array is of length 0, return right array
    if len(left) == 0:
        return right
    # If right array is of length 0, return left array
    if len(right) == 0:
        return left
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    midpoint = len(numbers) // 2
    left = numbers[:midpoint]
    right = numbers[midpoint:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# Test the merge function
if __name__ == "__main__":
    left = [1, 3, 5]
    right = [2, 4, 6]
    merged = merge(left, right)
    print("Merged array:", merged)  # Output: Merged array: [1, 2, 3, 4, 5, 6]

    # Now test the merge_sort function
    unsorted_numbers = [38, 27, 11, 43, 3, 9, 82, 10]
    sorted_numbers = merge_sort(unsorted_numbers)
    print("Sorted array:", sorted_numbers)  # Output: Sorted array: [3, 9, 10, 11, 27, 38, 43, 82]