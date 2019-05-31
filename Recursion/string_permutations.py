# Problem Statement
# Given an input string, return all permutations of the string in an array.

# Example 1:

# string = 'ab'
# output = ['ab', 'ba']
# Example 2:

# string = 'abc'
# output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']


def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    perm = []
    if len(string) <= 1:
        perm.append(string)
    else:
        first_char = string[0]
        remain = string[1:]
        sub_perm = permutations(remain)
        for p in sub_perm:
            for i in range(0,len(p)+1):
                new_string = p[:i] + first_char + p[i:]
                perm.append(new_string)
    return perm


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


#Test 1
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

#Test 2
string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

#Test 3
string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)


