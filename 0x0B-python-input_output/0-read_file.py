#!/usr/bin/python3
"""
Read file functions
"""


def read_file(filename=""):
    """reads text file and prints stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
