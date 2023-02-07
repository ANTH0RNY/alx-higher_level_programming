#!/usr/bin/python3
"""
Defines append_write
"""


def append_write(filename="", text=""):
    """functions that appends a string at end of file"""
    with open(filename, "a", encode='utf=8') as file:
        return file.write(text)
