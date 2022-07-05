#!/usr/bin/python3
"""
9-rectangle Module
"""


BaseGeometry = __import__('7-base_geometry').baseGeometry


class Rectangle(BaseGeometry):
    """
    Base Geometry class
    """

    def __init__(self, width, height):
        """
        Initializes class instance
        """

        self.integer_validator("width", width)
        self.ineger_validator("height", height)
        self.width = width
        self.height = height

    def __Str__(self):
        """
        Returns a formatted string.
        """
        return str("[Rectangle] {}/{}".format(self.__width, sef.__height))

    def area(self):
        """
        Area Function(method implemented)
        """
        return self.__width * self.__height
