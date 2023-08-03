# Define division function

def safe_print_division(a, b):
    try:
        result = a / b
        # Division by zero exception
        
    except ZeroDivisionError:
            return None
    else:
         return result
    finally:
        if b == 0:
            result = None
            print("Inside result: {}".format(result))
        else:
            print("Inside result: {}".format(result))
    

 
# safe_print_division(10,0)



