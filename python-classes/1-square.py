"""
This is module docstring for size validation task..
"""
class Square:
    def __init__(self, size = 0):
        self.__size = size
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
Square.__doc__ = """ A class that defines a square by """