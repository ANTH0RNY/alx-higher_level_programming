#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle:
    """ Empty Rectangle class """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Agrs:
                none
            Return:
                none
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for private property width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for private property height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for private attribute height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.width * self.__height

    def perimeter(self):
        """ returns perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ returns print of rectangle """
        out = ""
        if self.__width != 0 and self.__height != 0:
            out += "\n".join("#" * self.__width for i in range(self.__height))
        return out

    def __repr__(self):
        """
            should return a string representation of the rectangle to be
            able to recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d}".format(self.__width, self.__height)
