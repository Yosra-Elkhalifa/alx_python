"""
A module related to Python Almost a circle project 
that has a class Rectangle that inherits from Base 
- Has private attributes: __width , __height , __x , __y 
- Class constructor: 

"""
from models.base import Base

class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    private instanve attriubtes:
    1- width
    3- height
    4- x
    5- y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A constructor method to instatiate instances with arguments 
        Validates arguments accordingly 
        """
        super().__init__(id)
        # width validation
        if type(width) != 'int':
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width
        # height validation
        if type(height) != 'int':
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height
        # x validation
        if type(x) != 'int':
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = x
        # y validation
        if type(y) != 'int':
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = y


    @property
    def width(self):
        """
        Width getter method
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Width setter method
        Validates that the input is inteager and greater than zero
        """
        if type(value) != 'int':
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        """
        Height getter method
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Height setter method
        Validates that the input is inteager and greater than zero
        """
        if type(value) != 'int':
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Attributet x getter method
        """
        return self.__x
    @x.setter
    def x(self, value):
        """
        Attribute x setter method
        Validates that the input is inteager and greater than or equals zero
        """
        if type(value) != 'int':
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        """
        Attribute y getter method
        """
        return self.__y
    @y.setter
    def y(self, value):
        """
        Attribute y setter method
        Validates that the input is inteager and greater than or equals zero
        """
        if type(value) != 'int':
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value



    
