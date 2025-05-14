#!/usr/bin/python3
"""Print the sum of all arguments."""
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total = sum(int(x) for x in args)
    print(total)
