#!/usr/bin/python3
"""Python coding shebang"""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #."""
        if self.___size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(o, self.__size):
                    print("#", end="")
                print()
