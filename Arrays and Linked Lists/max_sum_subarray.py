# Problem Statement
# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

# Example 1:

# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.
# Example 2:

# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
#     max_sum = 0
#     i = 0
#     for i in range(len(arr)-1):
#         sum_current = 0
#         for j in arr[i:]:
#             sum_current += j
#             max_sum = max(max_sum , sum_current)
#     return max_sum

#     max_sum = arr[0]
#     current_sum = arr[0]

#     for num in arr[1:]:
#         current_sum = max(current_sum + num, num)
#         max_sum = max(current_sum, max_sum)
#     return max_sum
    
    current_sum = 0
    max_sum = 0
    start = 0 
    i = 0
    end = 0
    s = 0
    for num in arr:
        current_sum = max(current_sum + num,num)
        if current_sum < 0:
            max_sum = 0; 
            s = i + 1;
        if max_sum <= current_sum:
            max_sum = current_sum
            start = s; 
            end = i; 
        i += 1
    print("From {} to {}".format(start, end))
    print(arr[start:end+1])
    return max_sum
    
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

#Test 1
arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

#Test 2
arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

#Test 3
arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)
