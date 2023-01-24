#!/usr/bin/python3
''' defines class square '''


class Square:
    """Represents a square
    Attributes:
        __size (int): size of sides of the square
    """
    def __init__(self, size=0, position=0):
        """Init a square
        Args:
           size (int): size of the sides of a square
        Returns: none
        """
        self.size = size
        self.position = position

    def area(self):
        """Gets the area of a square
           Args: none
           Returns:
                int: area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter for self
            Returns:
                size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
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

    def my_print(self):
        """Prints the square
            Args: none
            Returns: none
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
