"""
A module that have a function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""
def is_same_class(obj, a_class):
    """
    A function that have two arguments: object and class 
    returns True if the object is instance of the class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
