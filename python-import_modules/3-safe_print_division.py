# Define division function

def safe_print_division(a, b):
    try:
        result = a / b
        # Division by zero exception
    except ZeroDivisionError:
         if b == 0:
            return None
         else:
            return result
    finally:
        print("Inside result: {}".format(result))

    return result

# a = 10
# b = 0    
# result = safe_print_division(a,b)



