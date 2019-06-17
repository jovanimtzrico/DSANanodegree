# Problem statement
# Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.

# For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).

# The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .

def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
        
    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start 
    # index and the end index
    
    index = binary_search(arr, number, 0, len(arr)-1)
    min_index = index
    max_index = index
    min_temp_index = 0
    max_temp_index = 0
    while min_temp_index != -1 and max_temp_index != -1:
        min_temp_index = binary_search(arr, number, 0, min_index-1)
        max_temp_index = binary_search(arr, number, max_index+1, len(arr)-1)
        if min_temp_index != -1:
            min_index = min(min_index, min_temp_index)
        if max_temp_index != -1:
            max_index = max(max_index, max_temp_index)
            
    return [min_index,max_index]

def binary_search(array, target, start, end):
    if start > end:
        return -1
    while start <= end:
        middle = (start + end)//2
        if target == array[middle]:
            return middle
        if target < array[middle]:
            return binary_search(array, target, start, middle-1)
        else:
            return binary_search(array, target, middle + 1, end)

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

#Test 1
input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

#Test 2
input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

#Test 3
input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

#Test 4
input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
