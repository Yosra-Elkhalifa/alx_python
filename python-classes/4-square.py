"""
This is module docstring for size validation task..
"""
class Square:
   
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
        if value != int(value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Area of square function"""
        return self.__size ** 2
    def my_print(self):
        """Method that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(0,self.__size):
            for j in range(0,self.__size):
                print("#", end="")
            print()
        
        
Square.__doc__ = """ A class that defines a square by """
