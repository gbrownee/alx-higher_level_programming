#!/usr/bin/python3
"""
11-square Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class
    """

    def __init__(self, size):
        """
        Initializes a Square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a formatted string
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """
        Area function(must be implemented)
        """
        return self.__size ** 2
