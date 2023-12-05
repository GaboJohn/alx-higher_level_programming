#!/usr/bin/python3

"""Defines a function for saving an object to a text file with JSON representation."""


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of the given object to a text file."""
    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)

