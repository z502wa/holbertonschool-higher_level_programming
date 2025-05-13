#!/usr/bin/python3
# 3-print_alphabt.py: prints the ASCII alphabet in lowercase except 'q' and 'e'
for code in range(97, 123):
    if code not in (101, 113):
        print("{:c}".format(code), end="")
