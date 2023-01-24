#!/usr/bin/python3
''' defines class square '''

class square:
    """Represents a square
    Attributes:
        __size (int): size of sides of the square
    """
    def __init__(self, size = 0):
        """Init a square
        Args:
           size (int): size of the sides of a square
        Returns: none
        Raises:
            TypeError: if the input is not an int
            ValueError: if input is less than 0
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
               self.__size = size
        else:
            raise TypeError('size must be an integer')
    def area(self):
        """Gets the area of a square
           Args: none
           Returns:
                int: area of square
        """
        return self.__size ** 2
