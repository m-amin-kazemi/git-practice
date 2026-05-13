def add(a, b):
    '''
    Returns the sum of a and b.
    This function takes two numbers as input and returns their sum.
    '''
    return a + b

def subtract(a, b):
    """
    Returns the difference of a and b.
    This function takes two numbers as input and returns the result of subtracting b from a.
    """
    return a - b        

def multiply(a, b):
    """
    Returns the product of a and b.
    This function takes two numbers as input and returns their product.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a and b.
    This function takes two numbers as input and returns the result of dividing a by b.
    Raises an error if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """
    Returns a raised to the power of b.
    This function takes two numbers as input and returns the result of a raised to the power of b.
    """
    return a ** b