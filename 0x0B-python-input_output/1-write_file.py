#!/usr/bin/python3
"""
writes a string to file
"""


def write_file(filename="", text=""):
    """ writes text to filename"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

