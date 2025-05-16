#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Return a list of booleans indicating if each integer is a multiple of 2.
    The returned list has the same length as the input list.
    """
    result = []
    for num in my_list:
        # Append True if num is divisible by 2, else False
        result.append(num % 2 == 0)
    return result
