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
            print("Getter function called")
            return size
        """Setter function"""
        @size.setter
        def size(self, value):
            self.__size = value
            print("setter function called")
        
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Area of square function"""
        return self.__size ** 2
        
Square.__doc__ = """ A class that defines a square by """
