#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """Getters"""
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """Setters"""
    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of rectangle"""
        return self.width * self.height

    def display(self):
        """Dsiplays rectangle with #"""
        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height)
