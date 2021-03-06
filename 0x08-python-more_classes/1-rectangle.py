#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """This is a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Inilization of the width and height of the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width variable of Square class instance """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value for Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height variable of Square class instance """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets heigth value for Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
