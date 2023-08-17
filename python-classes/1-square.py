"""
This is module docstring for size validation task..
"""
class Square:
    __size = None
    try:
        def __init__(self, size = 0):
            self.__size = size
    except TypeError:
            if  not isinstance(int,__size):
                raise TypeError("size must be an integer")
    except ValueError:
            if __size < 0:
                raise ValueError("size must be >= 0")
           
       

Square.__doc__ = """ A class that defines a square by """



