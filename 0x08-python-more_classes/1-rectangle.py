#!/usr/bin/python3
'''Module 1-rectangle.'''


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance

        Args:
        value: valueof the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """REtrieves the height of a rectangle instance."""
        return self.__height

    @height.setter
    def height(Self, value):
        """Sets the height of a REctangle instance.

        Args:
        value: value of the height, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
