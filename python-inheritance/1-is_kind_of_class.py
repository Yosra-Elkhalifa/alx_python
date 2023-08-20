"""
A module that have a function that returns True if the object is an instance of, 
or if the object is an instance of a class that inherited from, the specified class ;
 otherwise False.
"""
def is_kind_of_class(obj, a_class):
    """
    A function that have two arguments: object and class 
    returns True if the object is instance of the class
    or instance of a class that inherited from the specified class
    """
    if isinstance(obj,a_class):
        return True
    else:
        return False