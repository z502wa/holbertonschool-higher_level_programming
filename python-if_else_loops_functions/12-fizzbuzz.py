#!/usr/bin/python3
"""Module 12-fizzbuzz: prints numbers from 1 to 100 with FizzBuzz rules"""


def fizzbuzz():
    """Print numbers from 1 to 100 with Fizz/Buzz rules"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
