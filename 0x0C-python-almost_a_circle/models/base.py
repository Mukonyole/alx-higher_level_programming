#!/usr/bin/python3
"""
Defines base model class.
"""

class base:
    """
    Represents base model.
    """
    _nb_objects = 0
    def _int_(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
