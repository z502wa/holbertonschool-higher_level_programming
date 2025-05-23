#!/usr/bin/python3
"""
Provides the Square class to define a square with size and position.
"""


class Square:
    """
    Define a square and manage size and position attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): length of the square sides (default 0).
            position (tuple): printing offset as (horizontal, vertical) (default (0, 0)).

        Raises:
            TypeError: if size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: the side length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): new side length.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the printing position of the square.

        Returns:
            tuple: (horizontal spaces, vertical newlines).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the printing position with validation.

        Args:
            value (tuple): pair of non-negative integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: area (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using '#' character, respecting position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print("")

        # each row: horizontal offset + square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
[201~#!/usr/bin/python3
"""
Provides the Square class to define a square with size and position.
"""


class Square:
    """
    Define a square and manage size and position attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): length of the square sides (default 0).
            position (tuple): printing offset as (horizontal, vertical) (default (0, 0)).

        Raises:
            TypeError: if size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: the side length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): new side length.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the printing position of the square.

        Returns:
            tuple: (horizontal spaces, vertical newlines).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the printing position with validation.

        Args:
            value (tuple): pair of non-negative integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: area (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using '#' character, respecting position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print("")

        # each row: horizontal offset + square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
