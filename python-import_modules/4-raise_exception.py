def raise_exception():
    try:
        raise TypeError
    except TypeError:
        print("Exception has been raised")


raise_exception()