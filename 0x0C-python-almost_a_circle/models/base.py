#!/usr/bin/python3
"""Base class"""

import json
import csv

class Base:
    """This defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (dict): can be thought of as a double
            pointer to a dictionary
        """
        try:
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
        except TypeError:
            dummy = cls(1, 4)
            dummy.update(**dictionary)
            return dummy

    @staticmethod
    def draw(list_rectangles, list_squares):
        """that opens a window and draws all
        the Rectangles and Squares
        Args:
            list_rectangles : list of rectangles
            list_squares : list Squares
        """
        import turtle
        screen = turtle.Screen()
        screen.title("Rectangle or Square visualisation")
        t = turtle.Turtle()
        if type(list_rectangles) is list and len(list_rectangles) > 0:
            for rectangle in list_rectangles:
                rectangle = rectangle.to_dictionary()
                t.setpos(rectangle["x"], ["y"])
                t.pendown()
                t.forward(rectangle["width"])
                t.right(90)
                t.forward(rectangle["height"])
                t.right(90)
                t.forward(rectangle["width"])
                t.right(90)
                t.forward(rectangle["height"])
                t.penup()

        elif type(list_squares) is list and len(list_squares) > 0:
             for square in list_squares:
                square = square.to_dictionary()
                t.setpos(square["x"], ["y"])
                t.pendown()
                t.forward(square["size"])
                t.right(90)
                t.forward(square["size"])
                t.right(90)
                t.forward(square["size"])
                t.right(90)
                t.forward(square["size"])
                t.penup()

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        Args:
            json_string (str): is a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes from CSV"""
        with open("{}.csv".format(cls.__name__)) as f:
            data =  csv.reader(f)
        data = cls.from_json_string(data)
        lis = []
        for i in data:
            # i stopped here
            # for j in i:
            lis.append(cls.create(**i))
        return lis

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        with open("{}.json".format(cls.__name__)) as f:
            data =  f.read()
        data = cls.from_json_string(data)
        lis = []
        for i in data:
            lis.append(cls.create(**i))
        return lis

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ that serializes in CSV"""
        if list_objs is None or len(list_objs) == 0:
            with open("{}.csv".format(cls.__name__), newline='') as f:
                csv.writer([])
        else:
            list_dict = []
            for item in list_objs:
                list_dict.append(item.to_dictionary())
            if (cls.__name__ == "Rectangle"):
                data = [["id", "width", "height", "x", "y"]]
                for a_dict in list_dict:
                    inner = [
                            a_dict["id"],
                            a_dict["width"],
                            a_dict["height"],
                            a_dict["x"],
                            a_dict["y"]
                            ]
                    data.append(inner)
            elif (cls.__name__ == "Square"):
                data = [["id", "size", "x", "y"]]
                for a_dict in list_dict:
                    inner = [
                            a_dict["id"],
                            a_dict["size"],
                            a_dict["x"],
                            a_dict["y"]
                            ]
                    data.append(inner)
            with open("{}.csv".format(cls.__name__), newline='') as f:
                pen = csv.writer(f)
                pen.writerows(data)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None or len(list_objs) == 0:
            with open("{}.json".format(cls.__name__), mode="w") as f:
                f.write(cls.to_json_string(None))
        else:
            list_dict = []
            for item in list_objs:
                list_dict.append(item.to_dictionary())
            with open("{}.json".format(cls.__name__), "w") as f:
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

