#!/usr/bin/python3
"""
0-read_file Module
"""


def read_file(filename=""):
    """
    Reads from filename and prints
    its content to stdout
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
