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
        super().__init__(size, size,x,y,id)

    def __str__(self) -> str:
        """
        A method that  overriding the __str__ method so that it returns 
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,self.x,self.y,self.width)


