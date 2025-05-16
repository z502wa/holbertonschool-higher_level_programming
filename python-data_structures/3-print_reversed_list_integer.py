#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print each integer in the list in reverse order, one per line.
    """
    # Iterate over the list in reverse
    for number in my_list[::-1]:
        # Print integer using str.format()
        print("{:d}".format(number))
