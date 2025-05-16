#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print each integer in the list on a separate line.
    """
    for number in my_list:
        # Print integer using str.format()
        print("{:d}".format(number))
