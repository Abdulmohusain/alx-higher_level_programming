#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This defines the Rectangle class
    Args:
        Base: the base class that Reactangle inherits from
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("x", x)
        self.__x = x
        self.integer_validator("y", y)
        self.__y = y
        self.integer_validator("id", id)
        super().__init__(id)

    def area(self):
        """Computes the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.__height):
            for i in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def integer_validator(self, name, value):
        """Value validator"""
        # XX NO TEST XX
        # if type(name) is not str:
        #     raise TypeError("{} must be str".format(name))
        if name == "id" and value is None:
            return
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{:s} must be >= than 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{:s} must be > than 0".format(name))

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
        if len(args) == 0:
            return
        for n, arg in enumerate(args):
            if n == 0:
                self.id = arg
            elif n == 1:
                self.__width = arg
            elif n == 2:
                self.__height = arg
            elif n == 3:
                self.x = arg
            elif n == 4:
                self.y = arg

    def __str__(self):
        """nicely printable format of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                       self.id,
                                                       self.x,
                                                       self.y,
                                                       self.__width,
                                                       self.__height
                                                       )

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.integer_validator("y", value)
        self.__y = value
