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
            if not isinstance(int,size):
                print("size must be an integer")
        except ValueError:
            if size < 0:
                print("size must be >= 0")

           
       

Square.__doc__ = """ A class that defines a square by """



