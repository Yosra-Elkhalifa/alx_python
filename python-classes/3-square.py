"""
This is module docstring for size validation task..
"""
class Square:
    __size = None
    def __init__(self, size = 0):
        """Method to instantiate an object"""
        self.__size = size
        """Getter function"""
        @property
        def size(self):
            return self.__size
        """Setter function"""
        @size.setter
        def size(self, value):
            if size != int(size):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
    def area(self):
        """Area of square function"""
        return self.__size ** 2
        
Square.__doc__ = """ A class that defines a square by """
