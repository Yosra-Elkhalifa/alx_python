"""
This is module docstring for zero squre task
"""
class Square:
    __size = None
    try:
        def __init__(self, size = 0):
            self.__size = size
    except TypeError:
        if __size is not int:
            print("size must be an integer")
    except ValueError:
        if __size < 0:
            print("size must be >= 0")

Square.__doc__ = """ A class that defines a square by """



