#!/usr/bin/python3

'''Explains a function that adds integers.'''

def add_integer(a, b=98):
    '''
     Return the integer addition of a and b.

     Float arguments are typecasted to ints before addition is performed.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.

    Returns:
        int: The sum of a and b as an integer.
    '''

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or  isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
