#!/usr/bin/python3
"""
4-fron_json_string Module
"""


import json


def from_json_string(my_str):
    """
    Returns the object represented by my_str
    """

    return json.loads(my_str)
