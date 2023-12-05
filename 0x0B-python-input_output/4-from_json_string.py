#!/usr/bin/python3

"""Defines a function for converting a JSON string to a Python object."""


def from_json_string(my_str):
    """Return the Python object represented by the given JSON string."""
    import json

    return json.loads(my_str)
