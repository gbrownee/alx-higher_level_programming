#!/usr/bin/python3
"""Module 8-rectangle"""


class Rectangle:
    """Rectangle class defined by width and height"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance"""
