def raise_exception_msg(message=""):
    try:
        raise NameError
    except NameError:
        print(message)

# raise_exception_msg("C is Fun")