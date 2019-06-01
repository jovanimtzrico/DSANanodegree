# Problem Statement
# Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down.

def deep_reverse(arr):
    if len(arr) <= 1:
        return arr
    reverse = []
    for i in range(len(arr)-1, -1, -1):
        if isinstance(arr[i], list):
            arr[i] = deep_reverse(arr[i])
        reverse.append(arr[i])
    return reverse

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

#Test 1
arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)


#Test 2
arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

#Test 3
arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

#Test 4
arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)
