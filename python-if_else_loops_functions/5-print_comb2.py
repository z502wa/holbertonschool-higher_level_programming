#!/usr/bin/python3
# 5-print_comb2.py: prints numbers from 00 to 99 separated by ", "
for i in range(100):
    print(f"{i:02d}", end=", " if i < 99 else "\n")
