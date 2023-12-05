#!/usr/bin/python3

"""Defines a function for reading and printing the contents of a text file."""


def read_file(filename: str = "") -> None:
    """Read and print the contents of a UTF-8 text file."""
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
