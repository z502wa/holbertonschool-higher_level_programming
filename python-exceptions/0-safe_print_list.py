#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints the first x elements of my_list on the same line.
    Uses try/except to handle cases where x is greater than the list length.
    Returns the actual number of elements printed.
    """
    count = 0  # initialize printed element count and index
    while count < x:
        try:
            print("{}".format(my_list[count]), end="")  # print element without newline
            count += 1  # increment count/index
        except IndexError:
            # reached end of list, no more elements to print
            break
    print()  # newline after printing all elements
    return count  # return number of elements printed
