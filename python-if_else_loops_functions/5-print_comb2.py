#!/usr/bin/python3
# 5-print_comb2.py: prints numbers from 00 to 99 separated by ", "
for i in range(99):
    print("{:02d}".format(i), end=", ")
print("{:02d}".format(99))
