#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    count = 0
    for element in range(x):
        # We use the try statment incase the proccess is susseful
        try:
            print("{}".format(my_list[element]), end="")
            count += 1
            # The exception encounters the error for out of range index
            # it will break out of the loop if error occured
        except IndexError:
            break
    print()
    return count
