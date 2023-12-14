#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attributes in order: id, size, x, y."""
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
        elif kwargs:
            self.id = int(kwargs.get('id', self.id))
            self.size = int(kwargs.get('size', self.size))
            self.x = int(kwargs.get('x', self.x))
            self.y = int(kwargs.get('y', self.y))

        if not isinstance(self.size, int) or self.size <= 0:
            raise ValueError("size must be a positive integer")
        if not isinstance(self.x, int) or self.x < 0:
            raise ValueError("x must be a non-negative integer")
        if not isinstance(self.y, int) or self.y < 0:
            raise ValueError("y must be a non-negative integer")

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
