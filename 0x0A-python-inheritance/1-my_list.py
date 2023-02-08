#!/usr/bin/python3
"""
Defines the Mylist class
"""


class MyList(list):
    """inhertites from list"""
    def __init__(self):
        """Init the class"""
        super.__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
