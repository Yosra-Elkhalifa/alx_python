# Define division function

def safe_print_division(a, b):
    try:
        result = a / b
        # Division by zero exception
    except ZeroDivisionError:
         result = 'None'
    finally:
        print("Inside result: {}".format(result))

    

safe_print_division(10, 2)


