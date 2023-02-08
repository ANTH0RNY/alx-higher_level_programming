#!/usr/bin/python3
"""
has inherites_from
"""


def inherits_from(obj, a_class):
    """CHECKS IF A SUB CLASS"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
