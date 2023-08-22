"""
A module that have a class Square that inherits from Rectangel
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class that inherits from class Rectangle
    Square class has constructor class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        A constructor class with Rectangle arguments
        """
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        self.size = super().__init__(self.width)
        self.size = super().__init__(self.height)
        self.validate_width()
        self.validate_height()
        self.validate_x()
        self.validate_y()

    def __str__(self):
        """
        A method that  overriding the __str__ method so that it returns 
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}/{}".format(self.id,self.__x,self.__y,self.__width)

