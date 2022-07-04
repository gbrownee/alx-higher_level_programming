#!/usr/bin/python3
"""Module 7-base_geometry.
Creates a BaseGeometry class
"""


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """Raises an Exception with message
        'area() is not implemented'.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
