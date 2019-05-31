# Reversing a String
# The goal in this notebook will be to get practice with a problem that is frequently solved by recursion: Reversing a string.

# Note that Python has a built-in function that you could use for this, but the goal here is to avoid that and understand how it can be done using recursion instead.


def reverse_string1(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that us reversed of input
    """
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char


def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    if input == "" or len(input) == 1:
        return input
    return input[len(input)-1] + reverse_string(input[:-1])


# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")

