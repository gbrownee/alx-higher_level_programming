#!/usr/bin/python3
"""
1-append_write Module
"""


def append_write(filename="", text=""):
    """
    Appends text to filename
    """

    with open(filename, 'a+') as f:
        return f.write(text)
