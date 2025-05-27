#!/usr/bin/python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module contains MyList class that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list

    This class extends the built-in list class by adding
    a method to print the list in sorted order
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order

        This method creates a sorted copy of the list and prints it
        without modifying the original list
        """
        print(sorted(self))
