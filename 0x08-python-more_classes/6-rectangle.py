#!/usr/bin/python3
"""Defines a class of Rectangle"""


class Rectangle:
    """Represent rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle instance

        Args:
        width (int): width of new rectangle
        height (int): height of new rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set/get method to set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Public method instance.
        Returns perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of rectangle
           Returns empty string if width or height is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for x in range(self.__height):
            [result.append('#') for n in range(self.__width)]
            if x != self.__height - 1:
                result.append('\n')
        return "".join(result)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to recreate a new instance using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print the message when an instance is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
