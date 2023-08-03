# Define division function

def safe_print_division(a, b):
    try:
        result = a / b
        # Division by zero exception
        
    except ZeroDivisionError:
            result = None
    finally:
        print("Inside result: {}".format(result))

    

a = 10
b = 0    
safe_print_division(a,b)



