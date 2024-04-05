#!/usr/bin/python3
"""Defines a function to add two integers."""


def add_integer(a, b=98):
    """Return addition results of a and b as integer.

    Float args are typecasted to ints before addition.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
