#!/usr/bin/python3

"""Defines a function for appending a string to the end of a text file (UTF8)."""


def append_write(filename: str = "", text: str = "") -> int:
    """Append a string to a UTF-8 text file and return the number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
    return (num_chars_added)
