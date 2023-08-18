"""
This is module docstring for size validation task..
"""
class Square:
    """Class Square"""
    __size = None
    def __init__(self, size = 0):
            """Create an instance of class Squre"""
            try:
                self.__size = size
                
            except TypeError:
                if size != int(size):
                    print ("size must be an integer")
            except ValueError:
                if size < 0:
                    print ("size must be >= 0")
          

        
       





