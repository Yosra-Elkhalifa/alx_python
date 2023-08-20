"""
A module that have a function that that returns True if the object is an instance 
of a class that inherited (directly or indirectly) from the specified class ; 
otherwise False.
"""
def inherits_from(obj, a_class):
    """
    A function that have two arguments: object and class 
    returns True if the object is instance of a class
    that inherited (directly or indirectly) from the specified class
    """
    if issubclass(type(obj),a_class):
        return True
    elif type(obj) != a_class:
         return False
    else: 
        return False