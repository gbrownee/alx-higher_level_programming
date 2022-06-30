#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Prevents user from instantiating new locked class attribute"""

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """Initializes locked class instance"""
        self.first_name = first_name
