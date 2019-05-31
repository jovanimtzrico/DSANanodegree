# Implement sum_integers(n) to calculate the sum of all integers from  1  to  𝑛  using recursion. For example, sum_integers(3) should return  6  ( 1+2+3 ).

def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n-1)

print("sum_integers(3): ",sum_integers(3))


# Recursive function that takes the sum of all numbers in an array. For example, the array of [5, 2, 9, 11] would sum to 27 (5 + 2 + 9 + 11).
def sum_array(array):
    if len(array) == 1:
        return array[0]
    
    return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print("sum_array([1, 2, 3, 4])",sum_array(arr))


# Factorial using recursion
# The factorial function is a mathematical function that multiplies a given number,  𝑛 , and all of the whole numbers from  𝑛  down to 1.

# For example, if  𝑛  is  4  then we will get:

# 4∗3∗2∗1=24

def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

# Test Cases
print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")

