#!/usr/bin/python3
"""
defines BaseGeometry Class
"""


class BaseGeometry:
    """class not defined yet"""
    def area(self):
        """not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if int"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
