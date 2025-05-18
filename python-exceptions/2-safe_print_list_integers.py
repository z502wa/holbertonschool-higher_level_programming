#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    # iterate over up to x elements of the list
    for i in range(x):
        try:
            # try to format and print the current element as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # if formatting fails (not an int), skip this element silently
            continue
    print()  # finish with a newline
    return count
