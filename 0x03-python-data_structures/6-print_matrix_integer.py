#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, item in enumerate(row):
            endspace = ' ' if i < len(row) - 1 else ''
            print("{:d}".format(item), end=endspace)
        print()
