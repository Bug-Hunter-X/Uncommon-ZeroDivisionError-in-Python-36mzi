def function_with_uncommon_error(a, b):
    if a == 0 or b == 0:
        return 0  # Or raise a more informative exception: raise ZeroDivisionError("Division by zero") 
    else:
        return a / b