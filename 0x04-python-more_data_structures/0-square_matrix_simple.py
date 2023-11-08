#!/usr/bin/python3
from typing import List

def square_matrix_simple(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []

    squared = [[c**2 for c in line] for line in matrix]
    return squared
