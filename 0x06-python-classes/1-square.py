#!/usr/bin/python3
''' defines class square '''


class Square:
    """Represents a square
    Attributes:
        __size (int): size of sides of the square
    """
    def __init__(self, size):
        '''Init a square
        Args:
           size (int): size of the sides of a square
        Returns: none
        '''
        self.__size = size
