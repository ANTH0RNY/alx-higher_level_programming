#!/usr/bin/python3
''' defines class square '''


class Square:
    """Represents a square
    Attributes:
        __size (int): size of sides of the square
    """
    def __init__(self, size=0):
        """Init a square
        Args:
           size (int): size of the sides of a square
        Returns: none
        """
        self.size = size

    def area(self):
        """Gets the area of a square
           Args: none
           Returns:
                int: area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter for __self
            Returns:
                size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for __size
            Args:
                value (int): The size of square
            Returns: none
        """

        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
