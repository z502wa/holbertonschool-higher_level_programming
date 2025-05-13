#!/usr/bin/python3
# 2-print_alphabet.py: prints the ASCII alphabet in lowercase without a newline
for code in range(97, 123):
    print("{:c}".format(code), end="")
