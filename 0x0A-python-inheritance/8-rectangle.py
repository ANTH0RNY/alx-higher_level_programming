#!/usr/bin/python3
"""
defines sub class rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """init the rctangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
