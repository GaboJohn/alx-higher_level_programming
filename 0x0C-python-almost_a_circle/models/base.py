#!/usr/bin/python3
"""Defines base model class"""

import json
import csv
import turtle

class Base:
    """Base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            If list_dictionaries is None or empty - the string "[]".
            Otherwise - the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        Returns:
            An instance with attributes set based on the given dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)

            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON string.

        The filename must be: <Class name>.json - example: Rectangle.json
        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances - the type of these instances         depends on cls.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        The filename must be: <Class name>.csv - example: Rectangle.csv
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from <Class name>.csv.

        Returns:
            list: A list of instances instantiated from the CSV file.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        pen = turtle.Turtle()
        pen.screen.bgcolor("white")
        pen.pensize(4)
        pen.shape("turtle")

        pen.color("blue")
        for rectangle in list_rectangles:
            pen.showturtle()
            pen.up()
            pen.goto(rectangle.x, rectangle.y)
            pen.down()
            pen.color("blue")
            for x in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
            pen.hideturtle()

        pen.color("red")
        for square in list_squares:
            pen.up()
            pen.goto(square.x, square.y)
            pen.down()
            for x in range(4):
                pen.forward(square.width)
                pen.left(90)
                pen.forwar(square.height)
                pen.left(90)
            pen.hideturtle()

        turtle.exitonclick()
