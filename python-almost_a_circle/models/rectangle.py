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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.validate_width()
        self.validate_height()
        self.validate_x()
        self.validate_y()

    def validate_width(self):
        """
        A method that validates width
        """
        if not isinstance(self.width,int):
            raise TypeError("width must be an integer")
        elif self.width <= 0:
            raise ValueError("width must be > 0")
    
    def validate_height(self):
        """
        A method that validates height
        """
        if not isinstance(self.height,int):
            raise TypeError("height must be an integer")
        elif self.height <= 0:
            raise ValueError("height must be > 0")
    
    def validate_x(self):
        """
        A method that validates x
        """
        if type(self.x) != 'int':
            raise TypeError("x must be an integer")
        elif self.x < 0:
            raise ValueError("x must be > 0")
    
    def validate_y(self):
        """
        A method that validates y
        """
        if type(self.y) != 'int':
            raise TypeError("y must be an integer")
        elif self.y < 0:
            raise ValueError("y must be > 0")


    @property
    def width(self):
        """
        Width getter method
        """
        return self.__width
    @width.setter
    def width(self, width):
        """
        Width setter method
        Validates that the input is inteager and greater than zero
        """
        if type(width) != 'int':
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @property
    def height(self):
        """
        Height getter method
        """
        return self.__height 
    @height.setter
    def height(self, height):
        """
        Height setter method
        Validates that the input is inteager and greater than zero
        """
        if type(height) != 'int':
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

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



    
