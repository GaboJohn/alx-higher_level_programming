#!/usr/bin/python3

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
        """Return the JSON serialization of a list of dicts."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes."""
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                fieldnames = cls.get_csv_fieldnames()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = cls.get_csv_fieldnames()
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [cls.convert_csv_dict_to_int(d) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def convert_csv_dict_to_int(dictionary):
        """Convert values in a CSV dictionary to integers."""
        return {k: int(v) for k, v in dictionary.items()}

    @classmethod
    def get_csv_fieldnames(cls):
        """Return the CSV fieldnames based on the class type."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]

    @staticmethod
    def draw_shapes(turt, color, shape_list):
        """Draw shapes using the turtle module."""
        for shape in shape_list:
            turt.showturtle()
            turt.up()
            turt.goto(shape.x, shape.y)
            turt.down()
            for _ in range(2):
                turt.forward(shape.width)
                turt.left(90)
                turt.forward(shape.height)
                turt.left(90)
            turt.hideturtle()

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        Base.draw_shapes(turt, "#ffffff", list_rectangles)

        turt.color("#b5e3d8")
        Base.draw_shapes(turt, "#b5e3d8", list_squares)

        turtle.exitonclick()
