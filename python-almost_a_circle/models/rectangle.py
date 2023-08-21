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
        A constructor method to instatiate instances 
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width getter method
        """
        return self.width
    @width.setter
    def width(self, value):
        """
        Width setter method
        """
        self.__width = value
    @property
    def height(self):
        """
        Height getter method
        """
        return self.height
    @height.setter
    def height(self, value):
        """
        Height setter method
        """
        self.__height = value

    @property
    def x(self):
        """
        Argument x getter method
        """
        return self.x
    @x.setter
    def x(self, value):
        """
        Argument x setter method
        """
        self.__x = value
    @property
    def y(self):
        """
        Argument y getter method
        """
        return self.y
    @y.setter
    def y(self, value):
        """
        Argument y setter method
        """
        self.__y = value

    
