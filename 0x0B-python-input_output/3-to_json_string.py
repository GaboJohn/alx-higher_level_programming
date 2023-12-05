#!/usr/bin/python3

"""Defines a function for converting an object to its JSON representation."""


def to_json_string(my_obj):
    """Return the JSON representation of the given object."""
    import json

    return json.dumps(my_obj)
