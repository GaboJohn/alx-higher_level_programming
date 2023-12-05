#!/usr/bin/python3

"""Defines a function for writing a string to a text file (UTF8)."""


def write_file(filename: str = "", text: str = "") -> int:
    """Write a string to a UTF-8 text file and return the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written


