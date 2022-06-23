#!/usr/bin/python3
"""Python coding shebang"""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0) -> None:
        """Initializes the data."""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """Returns the current square area."""
            return self.__size ** 2
