#!/usr/bin/python3
"""Print number of arguments and list them."""
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    count = len(args)

    if count == 0:
        print("{} arguments.".format(count))
    else:
        # Header line
        if count == 1:
            print("{} argument:".format(count))
        else:
            print("{} arguments:".format(count))
        # List each argument
        for idx, val in enumerate(args, 1):
            print("{}: {}".format(idx, val))
