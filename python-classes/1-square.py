"""
This is module docstring for size validation task..
"""
class Square:
    __size = None
    def __init__(self, size = 0):
        self.__size = size
        try:
            raise TypeError
            raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

           
       

Square.__doc__ = """ A class that defines a square by """



