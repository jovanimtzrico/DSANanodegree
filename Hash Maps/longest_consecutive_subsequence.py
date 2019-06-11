# Problem Statement
# Given list of integers that contain numbers in random order, write a program to find the longest possible sub sequence of consecutive numbers in the array. Return this subsequence in sorted order. The solution must take O(n) time

# For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5

# Note- If two arrays are of equal length return the array whose index of smallest element comes first.


def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution
    min_value = input_list[0]
    max_value = 0
    longest_dict = dict()
    # iterate over the list and store element in a suitable data structure
    for elem in input_list:
        min_value = min(min_value, elem)
        max_value = max(max_value, elem)
        longest_dict[elem] = elem
    
    # traverse / go over the data structure in a reasonable order to determine the solution
    longest = list()
    current_longest = list()
    for i in range(min_value, max_value+1):
        if i in longest_dict:
            current_longest.append(i)
        else:
            if len(current_longest) > len(longest):
                longest = current_longest
            current_longest = list()
    
    if len(current_longest) > len(longest):
        longest = current_longest
    return longest


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")



#Test 1
test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

#Test 2
test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
test_function(test_case_2)

#Test 3
test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)