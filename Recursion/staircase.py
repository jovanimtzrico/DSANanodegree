# Problem Statement
# Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has n steps? Write a recursive function to solve the problem.

# Example:

# n = 3
# output = 4
# The output is 4 because there are four ways we can climb the staircase:

# 1. 1 step +  1 step + 1 step
# 2. 1 step + 2 steps 
# 3. 2 steps + 1 step
# 4. 3 steps

def staircase(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)



def staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    TODO - write a recursive function to solve this problem
    """
    if n <= 1:
        return 1
    steps = 0
    for i in [1,2,3]:
        if n-i >= 0:
            steps += staircase(n-i)
    return steps

def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Inductive Hypothesis - ways to climb rest of the steps
    return staircase(n-1) + staircase(n-2) + staircase(n-3)        

def staircase(n):
    if n == 0:
        return 1
    steps = 0
    for i in [1,2,3]:
        if n-i >= 0:
            steps += staircase(n-i)
    return steps

def staircase(n,num_steps = [1,2,3]):
    if n < 0:
        return 0
    if n == 0:
        return 1
    steps = 0
    for i in num_steps:
        steps += staircase(n-i)
    return steps


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

#Test 1
n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)

#Test 2
n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)


#Test 3
n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)

